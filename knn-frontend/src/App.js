import React, { useState } from 'react';
import axios from 'axios';

import './App.css';

// components folder
import Navbar from './components/Navbar';
import SearchField from './components/SearchField';
import Node from './components/Node';
import Server from './components/Server';
import LocalClassification from './assets/phone_classification.mp4'
// simple mui components
// import TextField from '@mui/material/TextField';
import ImportExportIcon from '@mui/icons-material/ImportExport';
import Button from '@mui/material/Button';
import LoadingButton from '@mui/lab/LoadingButton';
import Waiting from './assets/waiting.png'

function App() {
  const [inputText, setInputText] = useState("");
  const [loading, setLoading] = useState(false);

  const loadingIconsCount = 8;
  const loadingIcons = Array.from({ length: loadingIconsCount }, (_, index) => index + 1); // Create an array [1, 2, 3, 4, 5]

  const [noInputAtAll, setNoInputAtAll] = useState(true);

  const [data, setData] = useState({
    'payload': {
        'server': {
            'class': 0,
            'spam': 50
        },
        'clients': [
            {'class': 0,'spam': 50, 'isPoisned':false},
            {'class': 1,'spam': 50, 'isPoisned':false},
            {'class': 0,'spam': 50, 'isPoisned':false},
        ]
    },
    'status': 'success'
})


  const submitText=()=>{
    // alert("hi "+inputText);
    classifyInputRequest();
  }
  const classifyInputRequest = async () => {
    setLoading(true);
    setNoInputAtAll(false);
    try {
        const response = await axios.get(`http://127.0.0.1:5000/api/v1/classify?text=${inputText}`, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        await new Promise(r => setTimeout(r, 1500));
        setData(response.data);
        console.log(response)
    } catch (error) {
        console.log(error);
    } finally {
        setLoading(false);
    }
};
  return (
    <div className="App">
      {/* <Navbar/> */}
      <div className="content">
        <div className="content_input">
          {/* <form> */}
            <SearchField submitText={submitText} inputText={inputText} setInputText={setInputText}/>
            <LoadingButton loading={loading} variant="contained" sx={{ marginLeft:'10px', background:'var(--primary)', fontWeight:'bolder', color:'var(--primary-bg)', height:'50px' }} onClick={submitText}>{loading? 'Classify':'Classify'}</LoadingButton>
          {/* </form> */}
        </div>
        {!noInputAtAll && <div className="content_visuals">
          <div className="server_content">
            {!loading && <Server isPoisoned={false} SpamPer={data['payload']['server']['spam']}/>}
          </div>
          <div className="loading_content">
          {loading && (
            <div className='import_icons_row'>
              {loadingIcons.map(index => (
              <div key={index} index={index} className='import_export_container'>
                <ImportExportIcon className='import_export'/>
              </div>
              ))}
            </div>
          )}
          </div>
          <div className='nodes_content'>
            {!loading && <div className="nodes_container">
              <Node isPoisoned={data['payload']['clients'][0]['isPoisned']} SpamPer={data['payload']['clients'][0]['spam']}/>
              <Node isPoisoned={data['payload']['clients'][1]['isPoisned']} SpamPer={data['payload']['clients'][1]['spam']}/>
              <Node isPoisoned={data['payload']['clients'][2]['isPoisned']} SpamPer={data['payload']['clients'][2]['spam']}/>
            </div>}
          </div>
        </div>}
        {noInputAtAll && <div className='noInput'>
            <img src={Waiting} className="waiting_img" alt="poisoned" />
            <div class='noInput_message'>
              <h2>Let's start by writing a text to be <span class='primary-color'>classified</span>!</h2>
            </div>
          </div>}
      </div>
    </div>
  );
}

export default App;
