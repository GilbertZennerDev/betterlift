# ⬆️ BetterLift: A Multi-Lift Scheduling Simulator 🏢

> **Tired of crappy glass lifts?** This project aims to implement a **smarter, more efficient** scheduling algorithm for a fleet of lifts, outperforming basic elevator systems by dynamically distributing passenger requests.

## ✨ Features

  * **Multi-Lift Management:** Manages a specified number of independent lift units.
  * **Intelligent Load Balancing:** New calls are automatically assigned to the lift with the **shortest current queue** to ensure optimal distribution and minimize wait times.
  * **Queue Sorting:** Each lift's queue is sorted to minimize travel distance and ensure passengers are served in the most efficient order (currently based on floor order).
  * **Simulation Engine:** Lifts "travel" between floors with a configurable `traveltime` delay, simulating real-world movement.
  * **Interactive Interface:** Allows for manual addition of floor requests during operation.

## 🛠️ Installation and Setup

This project is written in Python and uses standard libraries.

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/betterlift.git
    cd betterlift
    ```
2.  **Run the Script:**
    ```bash
    python better_lift.py  # Assuming your file is named better_lift.py
    ```

## ⚙️ How It Works (Usage)

When the script runs, it initializes the lifts and immediately enters the interactive interface to accept input.

1.  **Initial Run:**
    ```
    Enter your target level:
    ```
2.  **Input:** Type in a floor number (e.g., `5`, `-2`, `10`) and press Enter.
3.  **Simulation:** After the input, the `runLifts()` method begins, and you will see the lifts moving to fulfill the queue:
    ```
    Moving Lift #0 up to 1
    Moving Lift #1 up to 1
    ...
    Lift #0 has arrived at 5 arrival #1
    ```

### Configuration

The lift system is configured upon initialization in the `if __name__ == '__main__':` block:

```python
bl = BetterLift(4, .05)
```

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `liftcount` | The number of lifts in the fleet. | `4` |
| `traveltime` | The time (in seconds) it takes to travel between two adjacent floors. | `.05` (for fast simulation) |

## 💡 Planned Future Enhancements

The next steps will transform this simulator into a robust, real-time scheduler\!

  * **⚡ Real-Time Concurrency:** Implement `runLifts` in a separate thread/process so that the simulation runs *simultaneously* with the user input interface (`interface`).
  * **🗺️ Advanced Scheduling Algorithm:** Refine the queue sorting to account for current lift direction (e.g., serve floors in the current direction before reversing).
  * **🖥️ Command Line Interface (CLI):** Develop a cleaner, non-blocking interface to add requests every X seconds without interrupting the simulation output.
  * **✅ Pickup & Drop-off Requests:** Differentiate between calling a lift *to* your current floor and requesting a floor *from* inside the lift.

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

-----

## 📧 Contact

Your Name - [zennergilbert@gmail.com]

Project Link: [https://https://github.com/GilbertZennerDev/betterlift](https://https://github.com/GilbertZennerDev/betterlift)# BetterLift
