import NextAuth from 'next-auth'
import CredentialsProvider from 'next-auth/providers/credentials'

export const authOptions = {
  // 1) Credentials provider calling your FastAPI `/auth/login`
  providers: [
    CredentialsProvider({
      name: 'Email / Password',
      credentials: {
        email: { label: 'Email', type: 'email', placeholder: 'you@example.com' },
        password: { label: 'Password', type: 'password' }
      },
      async authorize(credentials) {
        // call your FastAPI login endpoint
        const res = await fetch(`${process.env.FASTAPI_URL}/auth/login`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email: credentials.email,
            password: credentials.password
          })
        })

        if (!res.ok) {
          // invalid credentials or inactive
          throw new Error('Invalid email or password')
        }
        const { access_token, token_type } = await res.json()

        // Optionally, fetch the user profile (e.g. /auth/me) if you have one:
        const profileRes = await fetch(`${process.env.FASTAPI_URL}/auth/me`, {
          headers: { Authorization: `${token_type} ${access_token}` }
        })
        const user = await profileRes.json()

        const roles = user.roles

        // Return an object containing at least { id, email, role }
        return { 
          id: user.id,
          email: user.email,
          roles
        }
      }
    })
  ],

  // 2) Session & JWT callbacks to persist your FastAPI role
  callbacks: {
    async jwt({ token, user }) {
      // first time JWT callback runs, `user` is the object returned from authorize()
      if (user) {
        token.roles = user.roles
      }
      return token
    },
    async session({ session, token }) {
      // send role to the client
      session.user.roles = token.roles
      return session
    }
  },

  // 3) Secure your cookies & set a secret
  secret: process.env.NEXTAUTH_SECRET,
  session: {
    strategy: 'jwt'
  },
  pages: {
    signIn: '/auth/login',    // point to your custom Next.js login page
    error: '/auth/login?error' 
  }
}

const handler = NextAuth(authOptions)
export { handler as GET, handler as POST }
