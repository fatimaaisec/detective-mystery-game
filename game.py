import os
from suspects import Suspect, get_all_suspects
from clues import Clue, get_all_clues

class Game:
    def __init__(self):
        self.suspects = get_all_suspects()
        self.clues = get_all_clues()
        self.collected_clues = []
        self.moves_left = 15
        self.game_over = False
        self.player_won = False
        
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        """Print game header"""
        print("=" * 60)
        print("🔍 DETECTIVE MYSTERY: SOLVE THE HEIST 🔍".center(60))
        print("=" * 60)
        print()
    
    def print_status(self):
        """Print current game status"""
        print(f"\n📋 Moves Left: {self.moves_left}")
        print(f"🔎 Clues Collected: {len(self.collected_clues)}/5")
        print("-" * 60)
    
    def introduction(self):
        """Game introduction"""
        self.clear_screen()
        self.print_header()
        print("""
Welcome, Detective! 🕵️

A priceless diamond has been stolen from the mansion!
Your job: Interview the 5 suspects and collect evidence to 
find out WHO committed the crime.

You have 15 moves to solve the case.
Each action (interview, investigate) costs 1 move.

Can you crack the case? Let's go!
        """)
        input("\nPress Enter to begin...")
    
    def show_menu(self):
        """Display main menu"""
        self.clear_screen()
        self.print_header()
        self.print_status()
        
        print("\n📌 What do you want to do?\n")
        print("1. 🗣️  Interview a suspect")
        print("2. 🔍 Investigate for clues")
        print("3. 📊 Check collected clues")
        print("4. 🎯 Make an accusation")
        print("5. ❌ Quit game")
        print() 
    def interview_suspect(self):
        """Let player interview a suspect"""
        print("\n🗣️  Who would you like to interview?\n")
        
        for i, suspect in enumerate(self.suspects, 1):
            print(f"{i}. {suspect.name}")
        print("0. Back to menu")
        
        choice = input("\nEnter choice: ").strip()
        
        if choice == "0":
            return
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(self.suspects):
                suspect = self.suspects[idx]
                print(f"\n--- Interview with {suspect.name} ---")
                print(f"Occupation: {suspect.occupation}")
                print(f"\n{suspect.interview()}")
                self.moves_left -= 1
                input("\nPress Enter to continue...")
            else:
                print("❌ Invalid choice!")
                input("Press Enter to continue...")
        except ValueError:
            print("❌ Invalid input!")
            input("Press Enter to continue...")
    
def investigate(self):
        """Player investigates and finds clues"""
        print("\n🔍 You investigate the crime scene...\n")
        
        if len(self.collected_clues) >= 5:
            print("You've already collected all available clues!")
            input("Press Enter to continue...")
            return
        
        # Find uncollected clues
        uncollected = [c for c in self.clues if c not in self.collected_clues]
        
        if uncollected:
            clue = uncollected[0]
            print(f"✨ You found a clue!")
            print(f"📌 {clue.description}")
            print(f"💡 Evidence: {clue.evidence}")
            self.collected_clues.append(clue)
            self.moves_left -= 1
        else:
            print("No more clues to find.")
        
        input("\nPress Enter to continue...")
    
def show_clues(self):
        """Display collected clues"""
        self.clear_screen()
        self.print_header()
        
        if not self.collected_clues:
            print("\n📋 No clues collected yet!\n")
        else:
            print("\n🔎 COLLECTED CLUES:\n")
            for i, clue in enumerate(self.collected_clues, 1):
                print(f"{i}. {clue.description}")
                print(f"   Evidence: {clue.evidence}\n")
        
        input("Press Enter to continue...")
    
def make_accusation(self):
        """Player makes final accusation"""
        print("\n🎯 Time to make your accusation!\n")
        print("Who do you think is the criminal?\n")
        
        for i, suspect in enumerate(self.suspects, 1):
            print(f"{i}. {suspect.name}")
        print("0. Cancel")
        
        choice = input("\nEnter choice: ").strip()
        
        if choice == "0":
            return
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(self.suspects):
                accused = self.suspects[idx]
                self.resolve_accusation(accused)
            else:
                print("❌ Invalid choice!")
                input("Press Enter to continue...")
        except ValueError:
            print("❌ Invalid input!")
            input("Press Enter to continue...")
    
def resolve_accusation(self, accused):
        """Check if accusation is correct"""
        self.clear_screen()
        self.print_header()
        
        if accused.is_criminal:
            print(f"\n✅ CORRECT! You caught the criminal!\n\n🎉 {accused.name} was indeed the one who stole the diamond!\n\nMotive: {accused.motive}")
            self.player_won = True
            self.game_over = True
        else:
            print(f"\n❌ WRONG! {accused.name} is not the criminal!\n\nYou accused an innocent person. Case closed... but unsolved.\nThe real criminal got away!")
            self.game_over = True
        
        input("\nPress Enter to continue...")
    
def check_game_over(self):
        """Check if game should end"""
        if self.moves_left <= 0:
            self.clear_screen()
            self.print_header()
            print("""
⏰ OUT OF MOVES!

You ran out of time to solve the case.
The criminal escaped, and the case remains unsolved.

Better luck next time, Detective! 🕵️
            """)
            self.game_over = True
            self.player_won = False
    
def show_ending(self):
        """Show game ending screen"""
        self.clear_screen()
        self.print_header()
        
        if self.player_won:
            print("""
🏆 CASE SOLVED! 🏆

Congratulations, Detective! You successfully solved the heist!
Your detective skills are outstanding!

Thanks for playing! 🎮
            """)
        else:
            print("""
😔 CASE UNSOLVED

The criminal escaped and the case remains a mystery.
Better luck next time, Detective!

Thanks for playing! 🎮
            """)
    
def play(self):
        """Main game loop"""
        self.introduction()
        
        while not self.game_over:
            self.show_menu()
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                self.interview_suspect()
            elif choice == "2":
                self.investigate()
            elif choice == "3":
                self.show_clues()
            elif choice == "4":
                self.make_accusation()
            elif choice == "5":
                print("\n👋 Thanks for playing!")
                return
            else:
                print("\n❌ Invalid choice! Please try again.")
                input("Press Enter to continue...")
            
            self.check_game_over()
        
        self.show_ending()


def main():
    """Main entry point"""
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
