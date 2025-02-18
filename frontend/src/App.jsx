import React, { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

const author = {
    firstName: "Kristina",
    lastName: "Ziegler"
}

const header = (
  <header>
    <div className='header-wrapper'>
        <h2>Books</h2>
    </div>
  </header>
)


function App() {

  return (
    [header]
  )
    
}

export default App;
