import logo from './logo.svg';
import './App.css';
import {useEffect} from 'react';
import io from 'socket.io-client';



function App() {
  const socket = io('http://3.34.87.77:5000/binder');

  useEffect(() => {
    socket.on('rtdata', data => console.log(data));
  }, []);
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>

      </header>
    </div>
  );
}

export default App;
