import matplotlib.pyplot as plt


class Reg_Exp_Utils:
    """
    This class visualizes the impact of automation and resilience on various IT roles using a scatter plot.

    Attributes:
        roles (list of tuples): A list of tuples where each tuple contains:
            - Role name (str)
            - Automation impact score (int): Higher values indicate more replaceable roles.
            - Resilience/future value score (int): Higher values indicate safer roles.
        x (list of int): A list of automation impact scores extracted from `roles`.
        y (list of int): A list of resilience/future value scores extracted from `roles`.
        labels (list of str): A list of role names extracted from `roles`.

    Methods:
        None explicitly defined. The main functionality is executed when the script is run directly.

    Execution:
        When executed as a standalone script, the class generates a scatter plot:
            - Each point represents an IT role.
            - The x-axis represents the automation impact (replaceability).
            - The y-axis represents resilience or future value (safety).
            - Points are annotated with role names for clarity.
            - The plot includes a title, axis labels, grid, and dynamic axis limits for better visualization.

    Visualization Details:
        - Points are styled with a sky-blue color, black edges, and slight transparency.
        - Role names are annotated near their respective points with a dark blue font.
        - The plot is displayed with a clean layout and adjustable axis limits.
    """

    roles = [
        ("Soln Arch", 2, 9),
        ("Prodt Eng", 3, 9),
        ("Secrty Eng", 2, 8),
        ("DevOps / SRE", 3, 8),
        ("Mid-level Devs", 5, 6),
        ("QA Testers", 6, 5),
        ("Legacy Specialists", 7, 3),
        ("Contract Coders", 9, 3),
        ("Junior Devs", 8, 2),
    ]

    x = [role[1] for role in roles]
    y = [role[2] for role in roles]
    labels = [role[0] for role in roles]

    if __name__ == "__main__":
        plt.figure(figsize=(12, 8))
        plt.scatter(x, y, s=300, c="skyblue", edgecolors="black", alpha=0.8)

        # Annotate each point with its label
        for i, label in enumerate(labels):
            plt.annotate(
                label,
                (x[i], y[i]),
                textcoords="offset points",
                xytext=(10, 10),
                ha="left",
                fontsize=13,
                color="darkblue",
                fontweight="medium",
            )

        # Add title and labels
        plt.title(
            "Impact of Spec/Vibe Coding on IT Roles",
            fontsize=20,
            fontweight="bold",
        )
        plt.xlabel("Automation Impact (higher = more replaceable)", fontsize=16)
        plt.ylabel("Resilience / Future Value (higher = safer)", fontsize=16)

        # Dynamic axis limits
        plt.xlim(min(x) - 1, max(x) + 1)
        plt.ylim(min(y) - 1, max(y) + 1)

        # Add grid and adjust layout
        plt.xticks(fontsize=13)
        plt.yticks(fontsize=13)
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.show()
