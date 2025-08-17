'use client'

import { useState, useEffect } from 'react'
import { signIn } from 'next-auth/react'
import { useRouter, useSearchParams } from 'next/navigation'

export default function LoginPage() {
  const [email, setEmail]       = useState('')
  const [password, setPassword] = useState('')
  const [error, setError]       = useState('')
  const router                  = useRouter()
  const params                  = useSearchParams()
  const success                 = params.get('success')

  useEffect(() => {
    // show a success message if redirected here after signup
    if (success === 'signup') {
      setError('Account created! You can now log in.')
    }
  }, [success])

  async function handleSubmit(e) {
    e.preventDefault()
    setError('')

    const res = await signIn('credentials', {
      redirect: false,
      email,
      password,
    })

    if (res.error) {
      setError(res.error)
    } else {
      router.push('/')
    }
  }

  return (
    <div className="max-w-md mx-auto mt-16 p-6 bg-white rounded shadow">
      <h1 className="text-2xl font-semibold mb-4">Log In</h1>
      {error && <p className="mb-4 text-red-500">{error}</p>}

      <form onSubmit={handleSubmit} className="space-y-4">
        <label>
          <span className="block mb-1">Email</span>
          <input
            type="email"
            value={email}
            onChange={e => setEmail(e.target.value)}
            required
            className="w-full px-3 py-2 border rounded"
          />
        </label>
        <label>
          <span className="block mb-1">Password</span>
          <input
            type="password"
            value={password}
            onChange={e => setPassword(e.target.value)}
            required
            className="w-full px-3 py-2 border rounded"
          />
        </label>
        <button
          type="submit"
          className="w-full py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
        >
          Log In
        </button>
      </form>

      <p className="mt-4 text-center text-sm">
        Don’t have an account?{' '}
        <button
          onClick={() => router.push('/auth/signup')}
          className="text-blue-600 hover:underline"
        >
          Sign up
        </button>
      </p>
    </div>
  )
}
