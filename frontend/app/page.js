'use client'

// Data Imports
import FaqInformation from '@/public/information/faqs'

// Component Imports
import FaqSection from '@/components/FaqSection'
import {HeroBanner, BannerWithTitleAndText } from '@/components/Banners'

export default function HomePage() {

  return (
    <>
        <HeroBanner
          title="Join the Movement"
          subtitle="Run your charity with transparency and trust."
          imageSrc="/images/hero.png"
          ctaText="Get Started"
          ctaLink="/auth/signup"
        />

        <BannerWithTitleAndText 
          title="Learn More"
          paragraph1='At Charity, we believe every cause deserves an engaging way to connect with supporters. Our platform helps charities run transparent, compliant ways to raise funds.'
          paragraph2='Built for nonprofits, by nonprofits, we focus on simplicity, security, and affordability.'
        />

        <FaqSection faqInformation = {FaqInformation}/>
    </>
  )
}
