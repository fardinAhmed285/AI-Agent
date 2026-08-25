from dotenv import load_dotenv
from src.advanced_agent.workflow import Workflow

load_dotenv()


def main():
    workflow = Workflow()
    print("Developer Tools Research Agent")

    while True:
        query = input("\n🔍 Developer Tools Query: ").strip() # strip() removes unnecessary spaces at the beginning and end.
        if query.lower() in {"quit", "exit"}:
            break

        if query:
            result = workflow.run(query)   # result is a ResearchState object
            print(f"\n📊 Results for: {query}")
            print("=" * 60)

            for i, company in enumerate(result.companies, 1):   #enumerate() gives me both the number and the company.
                # The '1' here means start counting from 1 instead of 0.

                print(f"\n{i}. 🏢 {company.name}")
                print(f"   🌐 Website: {company.website}")
                print(f"   💰 Pricing: {company.pricing_model}")
                print(f"   📖 Open Source: {company.is_open_source}")

                if company.tech_stack:
                    print(f"   🛠️  Tech Stack: {', '.join(company.tech_stack[:5])}")

                if company.language_support:
                    print(
                        f"   💻 Language Support: {', '.join(company.language_support[:5])}"
                    )

                if company.api_available is not None: # api_available can have three possible values: True,False,None
                    # so thats why we put if not none soo that it only prints API information if I actually have an answer.
                    api_status = (
                        "✅ Available" if company.api_available else "❌ Not Available"
                    )
                    print(f"   🔌 API: {api_status}")

                if company.integration_capabilities:
                    print(
                        f"   🔗 Integrations: {', '.join(company.integration_capabilities[:4])}"
                    )

                if company.description and company.description != "Analysis failed":
                    print(f"   📝 Description: {company.description}")

                print()

            if result.analysis:
                print("Developer Recommendations: ")
                print("-" * 40)
                print(result.analysis)


if __name__ == "__main__": #If I run this file directly, start the program by calling main().
    main()