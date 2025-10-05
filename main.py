from joker import Joker


def prompt_for_topic():
    while True:
        topic = input("Enter the topic for the joke (Default: any): ").strip().lower()
        if not topic:
            topic = "any"
        print(f"ℹ️ Selected topic: {topic}")
        return topic

def main():
    while True:
        try:
            topic = prompt_for_topic()
            joker = Joker(topic=topic)
            joker.tell_a_joke()
            break
        except (ValueError, OSError) as e:
            print(f"❌ Fetching a joke failed: {e}")
            retry = input("Do you want to retry? (Y/n): ").strip().lower() or 'y'
            if retry != 'y':
                break
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            break


if __name__ == '__main__':
    main()
