from rich.console import Console
from rich.prompt import Prompt
from agents.orchestrator import Orchestrator

console = Console()

def main():
    console.print("[bold purple]AiiDA AI Assistant[/bold purple] — type 'exit' to quit\n")
    orchestrator = Orchestrator()
    while True:
        user_input = Prompt.ask("[bold]You[/bold]")
        if user_input.lower() == "exit":
            break
        response = orchestrator.handle(user_input)
        console.print(f"\n[bold teal]Assistant:[/bold teal] {response}\n")

if __name__ == "__main__":
    main()