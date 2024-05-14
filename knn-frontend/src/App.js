import './App.css';

// components folder
import Navbar from './components/Navbar';
import SearchField from './components/SearchField';

// simple mui components
// import TextField from '@mui/material/TextField';


function App() {
  return (
    <div className="App">
      <Navbar/>
      <div className="content">
        <div className="content_input">
          <form>
            <SearchField/>
          </form>
        </div>
        <div className="content_visuals">
          Visuals
        </div>
      </div>
    </div>
  );
}

export default App;
