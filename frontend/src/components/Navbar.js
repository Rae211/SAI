// src/components/Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav>
      <ul>
        <li><Link to="/login">Login</Link></li>
        <li><Link to="/profile">Profile</Link></li>
        <li><Link to="/messaging">Messaging</Link></li>
        <li><Link to="/notifications">Notifications</Link></li>
        <li><Link to="/tasks">Tasks</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
