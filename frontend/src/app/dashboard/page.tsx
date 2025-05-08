'use client';

import { useEffect, useState } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import AddBookModal from '@/components/AddBookModal';
import BookSearch from '@/components/BookSearch';

interface Book {
  id: number;
  title: string;
  author: string;
  status: 'reading' | 'finished' | 'want_to_read';
  rating?: number;
  finished_date?: string;
  cover_id?: number;
  publish_year?: number;
}

export default function DashboardPage() {
  const { user, loading } = useAuth();
  const router = useRouter();
  const [books, setBooks] = useState<Book[]>([]);
  const [isAddModalOpen, setIsAddModalOpen] = useState(false);
  const [stats, setStats] = useState({
    total: 0,
    reading: 0,
    finished: 0,
    wantToRead: 0,
    averageRating: 0
  });

  useEffect(() => {
    if (!loading && !user) {
      router.push('/login');
    }
  }, [user, loading, router]);

  const fetchBooks = async () => {
    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/books`, {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
      });
      if (response.ok) {
        const data = await response.json();
        setBooks(data);
        calculateStats(data);
      }
    } catch (error) {
      console.error('Error fetching books:', error);
    }
  };

  useEffect(() => {
    if (user) {
      fetchBooks();
    }
  }, [user]);

  const calculateStats = (books: Book[]) => {
    const stats = {
      total: books.length,
      reading: books.filter(book => book.status === 'reading').length,
      finished: books.filter(book => book.status === 'finished').length,
      wantToRead: books.filter(book => book.status === 'want_to_read').length,
      averageRating: 0
    };

    const ratedBooks = books.filter(book => book.rating);
    if (ratedBooks.length > 0) {
      stats.averageRating = ratedBooks.reduce((acc, book) => acc + (book.rating || 0), 0) / ratedBooks.length;
    }

    setStats(stats);
  };

  const handleAddBook = async (book: {
    title: string;
    author: string;
    status: 'reading' | 'finished' | 'want_to_read';
    coverId?: number;
    publishYear?: number;
  }) => {
    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/books`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        },
        body: JSON.stringify({
          title: book.title,
          author: book.author,
          status: book.status,
          cover_id: book.coverId,
          publish_year: book.publishYear
        })
      });

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || 'Failed to add book');
      }

      await fetchBooks();
    } catch (error) {
      console.error('Error adding book:', error);
      throw error;
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-b from-white to-gray-50 dark:from-gray-900 dark:to-gray-800 flex items-center justify-center">
        <div className="text-xl text-gray-600 dark:text-gray-300">Loading...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-b from-white to-gray-50 dark:from-gray-900 dark:to-gray-800">
      <div className="container mx-auto px-4 py-8">
        {/* Welcome Section */}
        <div className="mb-8">
          <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
            <div>
              <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
                Welcome back, {user?.username}!
              </h1>
              <p className="text-gray-600 dark:text-gray-400 mt-2">
                Track your reading progress and discover new books.
              </p>
            </div>
            <div className="w-full md:w-96">
              <BookSearch
                onSelect={(book) => {
                  handleAddBook({
                    ...book,
                    status: 'want_to_read'
                  });
                }}
              />
            </div>
          </div>
        </div>

        {/* Stats Section */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4 mb-8">
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Total Books</h3>
            <p className="text-3xl font-bold text-blue-600 dark:text-blue-400">{stats.total}</p>
          </div>
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Currently Reading</h3>
            <p className="text-3xl font-bold text-green-600 dark:text-green-400">{stats.reading}</p>
          </div>
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Finished</h3>
            <p className="text-3xl font-bold text-purple-600 dark:text-purple-400">{stats.finished}</p>
          </div>
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Want to Read</h3>
            <p className="text-3xl font-bold text-yellow-600 dark:text-yellow-400">{stats.wantToRead}</p>
          </div>
          <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">Average Rating</h3>
            <p className="text-3xl font-bold text-red-600 dark:text-red-400">
              {stats.averageRating.toFixed(1)}
            </p>
          </div>
        </div>

        {/* Books Section */}
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow">
          <div className="p-6 border-b border-gray-200 dark:border-gray-700 flex justify-between items-center">
            <h2 className="text-2xl font-bold text-gray-900 dark:text-white">Your Books</h2>
            <button
              onClick={() => setIsAddModalOpen(true)}
              className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            >
              Add Book
            </button>
          </div>
          <div className="p-6">
            {books.length === 0 ? (
              <div className="text-center py-8">
                <p className="text-gray-600 dark:text-gray-400">No books added yet.</p>
                <button
                  onClick={() => setIsAddModalOpen(true)}
                  className="mt-4 px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
                >
                  Add Your First Book
                </button>
              </div>
            ) : (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {books.map((book) => (
                  <div key={book.id} className="bg-gray-50 dark:bg-gray-700 rounded-lg p-4">
                    <div className="flex gap-4">
                      {book.cover_id ? (
                        <img
                          src={`https://covers.openlibrary.org/b/id/${book.cover_id}-M.jpg`}
                          alt={book.title}
                          className="w-20 h-28 object-cover rounded shadow-md"
                        />
                      ) : (
                        <div className="w-20 h-28 bg-gray-200 dark:bg-gray-600 rounded flex items-center justify-center">
                          <span className="text-gray-400 dark:text-gray-500 text-4xl">📚</span>
                        </div>
                      )}
                      <div className="flex-1">
                        <h3 className="text-lg font-semibold text-gray-900 dark:text-white">{book.title}</h3>
                        <p className="text-gray-600 dark:text-gray-400">{book.author}</p>
                        {book.publish_year && (
                          <p className="text-sm text-gray-500 dark:text-gray-400">{book.publish_year}</p>
                        )}
                        <div className="mt-2 flex items-center justify-between">
                          <span className={`px-2 py-1 rounded text-sm ${
                            book.status === 'reading' ? 'bg-green-100 text-green-800' :
                            book.status === 'finished' ? 'bg-purple-100 text-purple-800' :
                            'bg-yellow-100 text-yellow-800'
                          }`}>
                            {book.status.replace('_', ' ')}
                          </span>
                          {book.rating && (
                            <span className="text-yellow-500">★ {book.rating}</span>
                          )}
                        </div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>

      <AddBookModal
        isOpen={isAddModalOpen}
        onClose={() => setIsAddModalOpen(false)}
        onAdd={handleAddBook}
      />
    </div>
  );
} 