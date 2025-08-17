'use client'

import { useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { useSession, signOut } from 'next-auth/react'
import Link from 'next/link'

export default function DashboardLayout({ children }) {
  const { data: session, status } = useSession()
  const router = useRouter()

  useEffect(() => {
    if (status === 'unauthenticated') {
      router.push('/auth/login')
    }
  }, [status, router])

  if (status !== 'authenticated') {
    return null  // or a loading spinner
  }

  return (
    <div className="flex min-h-screen">
      <aside className="w-64 bg-white shadow-md p-6">
        <div className="mb-8">
          <span className="block font-medium text-gray-700">
            {session.user.email}
          </span>
          <button
            onClick={() => signOut({ callbackUrl: '/' })}
            className="mt-2 px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600"
          >
            Log out
          </button>
        </div>
        <nav className="space-y-2">
          <Link href="/dashboard/participant" className="block text-gray-600 hover:text-gray-900">
            My Lotteries
          </Link>
          {/* …other links based on role… */}
        </nav>
      </aside>
      <main className="flex-1 p-8 bg-gray-50">
        {children}
      </main>
    </div>
  )
}
