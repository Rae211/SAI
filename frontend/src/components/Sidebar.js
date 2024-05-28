import React from 'react';
import { Link } from 'react-router-dom';

function Sidebar() {
  return (
    <aside className="sidebar">
      <nav>
        <ul>
          <li><Link to="/profile">Profile</Link></li>
          <li><Link to="/messaging">Messaging</Link></li>
          <li><Link to="/notifications">Notifications</Link></li>
          <li><Link to="/tasks">Tasks</Link></li>
        </ul>
      </nav>
    </aside>
  );
}

export default Sidebar;
