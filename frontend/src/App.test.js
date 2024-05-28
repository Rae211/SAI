import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import UserProfile from './components/UserProfile';
import Messaging from './components/Messaging';
import Notifications from './components/Notifications';
import Tasks from './components/Tasks';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <div className="container">
          <Sidebar />
          <main>
            <Switch>
              <Route path="/profile" component={UserProfile} />
              <Route path="/messaging" component={Messaging} />
              <Route path="/notifications" component={Notifications} />
              <Route path="/tasks" component={Tasks} />
              <Route path="/" exact component={UserProfile} />
            </Switch>
          </main>
        </div>
      </div>
    </Router>
  );
}

export default App;
