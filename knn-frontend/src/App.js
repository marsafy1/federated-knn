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


function App() {
  const loadingIconsCount = 8;
  const loadingIcons = Array.from({ length: loadingIconsCount }, (_, index) => index + 1); // Create an array [1, 2, 3, 4, 5]

  var isLoading = true;
  
  return (
    <div className="App">
      <Navbar/>
      <div className="content">
        <div className="content_input">
          {/* <form> */}
            <SearchField/>
          {/* </form> */}
        </div>
        <div className="content_visuals">
          <div className="server_content">
            <Server isPoisoned={false} SpamPer={20}/>
          </div>
          <div className="loading_content">
          {isLoading && (
            <div className='import_icons_row'>
              {loadingIcons.map(index => (
              <div key={index} index={index} className='import_export_container'>
                <ImportExportIcon className='import_export'/>
              </div>
              ))}
            </div>
          )}
          </div>
          <div className="nodes_content">
            <Node isPoisoned={true} SpamPer={80}/>
            <Node isPoisoned={false} SpamPer={30}/>
            <Node isPoisoned={true} SpamPer={20}/>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
