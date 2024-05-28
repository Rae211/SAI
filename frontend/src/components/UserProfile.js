// src/components/UserProfile.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function UserProfile() {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    axios.get('/api/profile')
      .then(response => setProfile(response.data))
      .catch(error => console.error('Error fetching profile:', error));
  }, []);

  if (!profile) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Profile</h2>
      <p>Name: {profile.name}</p>
      <p>Email: {profile.email}</p>
      {/* 更多的用户资料 */}
    </div>
  );
}

export default UserProfile;
