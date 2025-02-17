import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  axios.get('http://loacalhost:8000/books/').then(response => {console.log(response.data)})

  return ("hello")
    
}

export default App;
