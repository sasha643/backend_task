from queue_manager import QueueManager

initial_profiles = [
    "https://www.linkedin.com/in/dhruvrajsinh-solanki-774735255/recent-activity/all/"
]

queue_manager = QueueManager()

try:
    queue_manager.push_new_profiles(initial_profiles)
    print("Initial profiles seeded successfully.")
except Exception as e:
    print(f"Error seeding initial profiles: {e}")
