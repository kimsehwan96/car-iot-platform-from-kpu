import React from 'react'
import 'antd/dist/antd.css';
import { BrowserRouter as Router , Switch, Route } from 'react-router-dom';
import Home from './pages/Home';

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route path='/' component={Home} />
        </Switch>
      </Router>
    </div>
  )
}

export default App

