// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import UserLogin from './components/UserLogin';
import UserProfile from './components/UserProfile';
import Messaging from './components/Messaging';
import Notifications from './components/Notifications';
import TaskManagement from './components/TaskManagement';

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/login" element={<UserLogin />} />
          <Route path="/profile" element={<UserProfile />} />
          <Route path="/messaging" element={<Messaging />} />
          <Route path="/notifications" element={<Notifications />} />
          <Route path="/tasks" element={<TaskManagement />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

