import Link from 'next/link'
import Image from 'next/image'
import React from 'react'

export function BannerWithTitleAndText({
    title, 
    paragraph1 = '', 
    paragraph2 = ''}){

    return(
        <section className="container mx-auto px-6 py-16">
        <h3 className="text-3xl font-bold mb-6 text-center">{title}</h3>
        <div className="max-w-4xl mx-auto text-center text-gray-700 space-y-4">
            {paragraph1 && <p>{paragraph1}</p>}
            {paragraph2 && <p>{paragraph2}</p>}
        </div>
        </section>
    )
};

export function HeroBanner({
    title = 'Welcome!',
    subtitle = '',
    imageSrc = '/images/default-hero.png',
    ctaText = '',
    ctaLink = '#',
  }) {
    return (
      <section className="relative flex items-center justify-center h-96 bg-gray-100">
        <Image
          src={imageSrc}
          alt={title}
          fill
          className="object-cover brightness-75 object-bottom"
        />
        <div className="absolute text-center text-white px-4">
          <h2 className="text-4xl font-bold mb-4">{title}</h2>
  
          {subtitle && <p className="text-lg mb-6">{subtitle}</p>}
  
          {ctaText && ctaLink && (
            <Link
              href={ctaLink}
              className="px-6 py-3 bg-blue-600 rounded-lg text-white font-semibold hover:bg-blue-700"
            >
              {ctaText}
            </Link>
          )}
        </div>
      </section>
    );
  }
  