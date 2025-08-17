export default function FaqSection({faqInformation}) {

    return(
    <section className="bg-white py-16">
    <div className="container mx-auto px-6">
        <h3 className="text-3xl font-bold mb-6 text-center">Frequently Asked Questions</h3>
        <div className="max-w-3xl mx-auto space-y-4">
        {faqInformation.map((faq, idx) => (
            <details key={idx} className="border rounded-lg p-4">
            <summary className="font-medium cursor-pointer">
                {faq.question}
            </summary>
            <p className="mt-2 text-gray-600">{faq.answer}</p>
            </details>
        ))}
        </div>
    </div>
    </section>
    )
}