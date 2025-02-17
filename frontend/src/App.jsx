import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [books, setBooks] = useState([])

  useEffect(() => {
    axios.get('http://localhost:8000/books/')
      .then(response => {
        setBooks(response.data)
      })
      .catch(error => {
        console.error('There was an error fetching the books!', error)
      })
  }, [])

  return (
    <div>
      <h1>Books</h1>
      <ul>
        {books.map(book => (
          <li key={book.id}>{book.title}</li>
        ))}
      </ul>
    </div>
  )
}

export default App;
