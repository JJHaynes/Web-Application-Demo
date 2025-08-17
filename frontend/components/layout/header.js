import Link from "next/link"
import React from "react"
import { signOut } from 'next-auth/react'

export default function NavBar({session, status}){

    return(
        <header className="bg-white shadow">
            <nav className="container mx-auto px-6 py-4 flex justify-between items-center">
                <div className="flex items-center space-x-6">
                    <Link href="/" className="text-2xl font-bold">Charity</Link>
                    <Link href="/charities" className="text-gray-700 hover:text-gray-900">
                        Charities
                    </Link>
                </div>

                {status === 'authenticated' && session ? (
                <div className="flex items-center space-x-4">
                    <span className="text-gray-700">{session.user.email}</span>
                    <button
                    onClick={() => signOut({ callbackUrl: '/' })}
                    className="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600"
                    >
                    Log Out
                    </button>
                </div>
                ) : (
                <Link
                    href="/auth/login"
                    className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
                >
                    Log In / Sign Up
                </Link>
                )}
            </nav>
        </header>
    )
}