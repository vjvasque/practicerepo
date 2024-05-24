import './App.css';
import React, { useState } from 'react';
import { createUser } from './api'

function App() {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await createUser({name, email})
      console.log(response.data)
    } catch (err) {
      console.log(err)
    }
  }

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder='Name' value={name} onChange={(e) => setName(e.target.value)} />
        <input type="text" placeholder='email' value={email} onChange={(e) => setEmail(e.target.value)} />
        <button type="submit">Create Users</button>
      </form>
    </div>
  );
}

export default App;
