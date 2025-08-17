'use client'
import Image from 'next/image'
import Link from 'next/link'

export default function CharityCard({ id, name, imageSrc, description, pendingLotteries = []}) {
  return (
    <div className="border rounded-lg shadow-sm overflow-hidden">
      <div className="relative h-48 w-full">
      {imageSrc ? (
          <Image
            src={imageSrc}
            alt={`${name} logo`}
            fill
            className="object-cover"
          />
        ) : (
          <Image
            alt={`${name} logo`}
            fill
            className="object-cover"
          />
        )}
      </div>
      <div className="p-6">
        <h3 className="text-xl font-semibold mb-2">{name}</h3>
        <p className="text-gray-600 mb-4">{description}</p>
        <h4 className="font-medium mb-2">Pending Activities</h4>
        {pendingLotteries.length > 0 ? (
          <ul className="space-y-1">
            {pendingLotteries.map(lot => (
              <li key={lot.id}>
                <Link
                  href={`/lottery/${lot.id}`}
                  className="text-blue-600 hover:underline"
                >
                  {lot.title}
                </Link>
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-gray-500">No pending activities.</p>
        )}
      </div>
    </div>
  )
}