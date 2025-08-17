'use client'

import { useEffect, useMemo, useState } from 'react'
import { usePathname, useRouter, useSearchParams } from 'next/navigation'
import CharityCard from '@/components/charity/CharityCard'

const API_BASE = process.env.NEXT_PUBLIC_FASTAPI_URL

export default function CharitiesPage() {
  const pageSize = 9

  const [charities, setCharities] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  const totalItems = charities.length
  const totalPages = Math.max(1, Math.ceil(totalItems / pageSize))

  const router = useRouter()
  const pathname = usePathname()
  const searchParams = useSearchParams()
  const currentPage = Math.min(
    totalPages,
    Math.max(1, Number(searchParams.get('page') || 1))
  )

  useEffect(() => {
    async function fetchCharities() {
      try {
        setLoading(true)
        const res = await fetch(`${API_BASE}/charities/all`) 
        console.info(res.status)
        if (!res.ok) throw new Error('Failed to fetch charities')
        const data = await res.json()
        setCharities(data)
      } catch (err) {
        setError(err.message)
      } finally {
        setLoading(false)
      }
    }
    fetchCharities()
  }, [])

  const paginatedCharities = useMemo(() => {
    const start = (currentPage - 1) * pageSize
    const end = start + pageSize
    return charities.slice(start, end)
  }, [currentPage, charities])

  const setPage = (page) => {
    const params = new URLSearchParams(Array.from(searchParams.entries()))
    if (page <= 1) params.delete('page')
    else params.set('page', String(page))
    const query = params.toString()
    const url = query ? `${pathname}?${query}` : pathname
    router.replace(url, { scroll: false })
  }

  const goPrev = () => currentPage > 1 && setPage(currentPage - 1)
  const goNext = () => currentPage < totalPages && setPage(currentPage + 1)

  return (
    <main className="container mx-auto px-6 py-16">
      <h1 className="text-3xl font-bold mb-8">Charities</h1>

      {loading && <p>Loading charities...</p>}
      {error && <p className="text-red-500">{error}</p>}

      {!loading && !error && (
        <>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {paginatedCharities.map((charity) => (
              <CharityCard
                key={charity.id}
                id={charity.id}
                name={charity.name}
                imageSrc={charity.hero_image_url}
                description={charity.description}
                pendingLotteries={charity.pendingLotteries}
              />
            ))}
          </div>

          {/* Pagination */}
          <div className="mt-10 flex items-center justify-between">
            <button
              type="button"
              onClick={goPrev}
              disabled={currentPage === 1}
              className="px-4 py-2 rounded-lg border text-sm disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Previous
            </button>

            <div className="text-sm">
              Page <span className="font-semibold">{currentPage}</span> of{' '}
              <span className="font-semibold">{totalPages}</span>
            </div>

            <button
              type="button"
              onClick={goNext}
              disabled={currentPage === totalPages}
              className="px-4 py-2 rounded-lg border text-sm disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Next
            </button>
          </div>
        </>
      )}
    </main>
  )
}
