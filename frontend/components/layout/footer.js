export default function Footer({FooterDetails="Charity. All rights reserved."}){
    return(
        <footer className="bg-gray-800 text-white py-6">
        <div className="container mx-auto px-6 text-center">
            &copy; {new Date().getFullYear()} {FooterDetails}
        </div>
        </footer>
    )
}
