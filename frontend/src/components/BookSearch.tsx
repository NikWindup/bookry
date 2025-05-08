import { useState, useEffect, useCallback } from 'react';
import debounce from 'lodash/debounce';

interface BookSearchResult {
  key: string;
  title: string;
  author_name?: string[];
  cover_i?: number;
  first_publish_year?: number;
}

interface BookSearchProps {
  onSelect: (book: {
    title: string;
    author: string;
    coverId?: number;
    publishYear?: number;
  }) => void;
}

export default function BookSearch({ onSelect }: BookSearchProps) {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<BookSearchResult[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const searchBooks = async (searchQuery: string) => {
    if (!searchQuery.trim()) {
      setResults([]);
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch(
        `https://openlibrary.org/search.json?q=${encodeURIComponent(searchQuery)}&limit=5`
      );
      
      if (!response.ok) {
        throw new Error('Failed to fetch books');
      }

      const data = await response.json();
      setResults(data.docs || []);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
      setResults([]);
    } finally {
      setIsLoading(false);
    }
  };

  // Create a debounced version of searchBooks
  const debouncedSearch = useCallback(
    debounce((searchQuery: string) => {
      searchBooks(searchQuery);
    }, 300),
    []
  );

  // Update search when query changes
  useEffect(() => {
    debouncedSearch(query);
    // Cleanup debounce on unmount
    return () => {
      debouncedSearch.cancel();
    };
  }, [query, debouncedSearch]);

  const handleSelect = (book: BookSearchResult) => {
    onSelect({
      title: book.title,
      author: book.author_name?.[0] || 'Unknown Author',
      coverId: book.cover_i,
      publishYear: book.first_publish_year
    });
    setQuery('');
    setResults([]);
  };

  return (
    <div className="relative">
      <div className="mb-4">
        <div className="flex gap-2">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search for a book..."
            className="flex-1 rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
          />
          {isLoading && (
            <div className="flex items-center px-4">
              <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-blue-600"></div>
            </div>
          )}
        </div>
      </div>

      {error && (
        <div className="bg-red-50 border border-red-400 text-red-700 px-4 py-3 rounded relative mb-4" role="alert">
          <span className="block sm:inline">{error}</span>
        </div>
      )}

      {results.length > 0 && (
        <div className="absolute z-10 w-full bg-white dark:bg-gray-800 rounded-md shadow-lg border border-gray-200 dark:border-gray-700">
          <ul className="max-h-60 overflow-auto">
            {results.map((book) => (
              <li
                key={book.key}
                onClick={() => handleSelect(book)}
                className="p-4 hover:bg-gray-50 dark:hover:bg-gray-700 cursor-pointer border-b border-gray-200 dark:border-gray-700 last:border-b-0"
              >
                <div className="flex items-center gap-4">
                  {book.cover_i && (
                    <img
                      src={`https://covers.openlibrary.org/b/id/${book.cover_i}-S.jpg`}
                      alt={book.title}
                      className="w-12 h-16 object-cover rounded"
                    />
                  )}
                  <div>
                    <h3 className="font-medium text-gray-900 dark:text-white">{book.title}</h3>
                    <p className="text-sm text-gray-600 dark:text-gray-400">
                      {book.author_name?.[0] || 'Unknown Author'}
                      {book.first_publish_year && ` • ${book.first_publish_year}`}
                    </p>
                  </div>
                </div>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
} 