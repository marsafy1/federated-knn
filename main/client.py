
import pandas as pd
import numpy as np
import sys
import gdown
from MyRedis import MyRedis
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score, recall_score, accuracy_score, precision_score, f1_score
# CONFIGS

CLIENTS_COUNT = 2

CLIENT_ID = int(sys.argv[1]) if len(sys.argv) > 1 else 0  # Default to 0 if no argument is provided


file_url = 'https://drive.google.com/uc?id=1H1hmjryGXbrXgGOLPRy7iKhBTIg2hEXt'
file_path = '../datasets/spam.csv'

X_train,X_test,y_train,y_test = None, None, None, None
local_data = None
clf = None
redisObject = MyRedis()

def get_dataset_from_drive():
    output = 'dataset.csv'  # Specify the local filename to save the downloaded file, with the correct file extension
    gdown.download(file_url, output, quiet=False)

def get_and_process_data():
    global local_data
    data = pd.read_csv(file_path)
    chunks = np.array_split(data, CLIENTS_COUNT)
    local_data = chunks[CLIENT_ID]
    # print(local_data)
    local_data['Spam']=local_data['Category'].apply(lambda x:1 if x=='spam' else 0)

def train_model():
    global clf, X_train, X_test, y_train, y_test
    X_train,X_test,y_train,y_test=train_test_split(local_data.Message,local_data.Spam,test_size=0.20)
    clf=Pipeline([
        ('vectorizer',CountVectorizer()),
        ('nb',KNeighborsClassifier(3))
    ])
    clf.fit(X_train,y_train)

def test_model():
    y_pred = clf.predict(X_test)
    y_probs = clf.predict_proba(X_test)[:, 1]  # Probabilities for the positive class
    auc = roc_auc_score(y_test, y_probs)
    recall = recall_score(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1-Score: {f1:.2f}")
    print(f"AUC Score: {auc:.2f}")

def init_model():
    get_and_process_data()
    train_model()
    # test_model()

def handle_input(input):
    predicted_class = clf.predict([input])[0]
    redisObject.publish_message('classification', f'client_{CLIENT_ID}', predicted_class)
    return predicted_class

if __name__ == '__main__':
    print(f"Client {CLIENT_ID} up and running...")
    init_model()
    for message in redisObject.get_pubsub().listen():
        message_type = message['type']
        if message['type'] == 'message':
            message = message['data'].decode()
            message_type = message.split("#")[0]
            sender = message.split("#")[1]
            message_content = message.split("#")[2]
    
            if(message_type == 'client_task'):
                print(f"I'm @client_{CLIENT_ID} - will classify => " + message_content)
                classification = handle_input(message_content)
                print(f"I'm @client_{CLIENT_ID} - classified " + message_content + " as => " + str(classification))
    
    
            if(message_type == "TERMINATE"):
                break

