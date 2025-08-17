'use client'

import { useState }    from 'react'
import { useRouter }   from 'next/navigation'

export default function SignupPage() {
  const [email,      setEmail]      = useState('')
  const [password,   setPassword]   = useState('')
  const [confirm,    setConfirm]    = useState('')
  const [error,      setError]      = useState('')
  const router                      = useRouter()

  async function handleSubmit(e) {
    e.preventDefault()
    setError('')

    if (password !== confirm) {
      setError('Passwords must match.')
      return
    }

    try {
      const res = await fetch(
        `http://localhost:8000/auth/signup`,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email, password }),
        }
      )
      const data = await res.json()
      if (!res.ok) {
        throw new Error(data.detail || 'Signup failed.')
      }
      // on success, redirect to login with a flag
      router.push('/auth/login?success=signup')
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <div className="max-w-md mx-auto mt-16 p-6 bg-white rounded shadow">
      <h1 className="text-2xl font-semibold mb-4">Sign Up</h1>
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
        <label>
          <span className="block mb-1">Confirm Password</span>
          <input
            type="password"
            value={confirm}
            onChange={e => setConfirm(e.target.value)}
            required
            className="w-full px-3 py-2 border rounded"
          />
        </label>
        <button
          type="submit"
          className="w-full py-2 bg-green-600 text-white rounded hover:bg-green-700"
        >
          Create Account
        </button>
      </form>

      <p className="mt-4 text-center text-sm">
        Already have an account?{' '}
        <button
          onClick={() => router.push('/auth/login')}
          className="text-blue-600 hover:underline"
        >
          Log in
        </button>
      </p>
    </div>
  )
}
