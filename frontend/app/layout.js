'use client'

import '../styles/globals.css'
import { SessionProvider, useSession } from 'next-auth/react'
import NavBar from '@/components/layout/header'
import Footer from '@/components/layout/footer'

function LayoutShell({ children }) {
  const { data: session, status } = useSession()

  return (
    <div className="flex flex-col min-h-screen">
      
      <header className="bg-white shadow">
        <NavBar session={session} status={status} />
      </header>

      <main className="flex-1 flex flex-col">{children}</main>

      <Footer />
    </div>
  )
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <SessionProvider>
          <LayoutShell>
            {children}
          </LayoutShell>
        </SessionProvider>
      </body>
    </html>
  )
}
