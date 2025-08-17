// app/error.js
'use client';  // this file must be a client component

import { useEffect } from 'react';

export default function GlobalError({ error, reset }) {
  useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h2 className="text-2xl font-semibold text-red-600">Something went wrong!</h2>
      <pre className="mt-2 text-sm text-gray-700">{error.message}</pre>
      <button
        className="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        onClick={() => reset()}
      >
        Try again
      </button>
    </div>
  );
}
