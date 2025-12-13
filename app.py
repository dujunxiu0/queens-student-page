import gradio as gr

def parse_list(text: str):
    """
    Convert a comma-separated string into a list of integers.
    - Extra spaces are ignored.
    - Empty items are skipped.
    - Raises ValueError if any item is not an integer.
    """
    nums = []
    for part in text.split(","):
        part = part.strip()
        if part == "":
            continue  # ignore empty cells
        try:
            nums.append(int(part))
        except:
            raise ValueError("Please enter only integers separated by commas.")
    if not nums:
        raise ValueError("Please enter at least one integer.")
    return nums

# Binary Search logic (returns all step-by-step messages)

def binary_search_steps(nums, target):
    """
    Run binary search on the sorted version of nums.
    Returns:
        found (bool),
        index (int or None),
        steps (list of text messages),
        sorted_nums (list)
    """

    nums_sorted = sorted(nums)
    low = 0
    high = len(nums_sorted) - 1
    steps = []
    step = 1

    while low <= high:
        mid = (low + high) // 2

        # Record each step clearly
        steps.append(
            f"Step {step}: low={low}, high={high}, mid={mid}, value={nums_sorted[mid]}"
        )

        # Check the mid position
        if nums_sorted[mid] == target:
            steps.append(f"→ Found {target} at index {mid}")
            return True, mid, steps, nums_sorted

        # Move right
        elif nums_sorted[mid] < target:
            steps.append(f"→ {nums_sorted[mid]} < {target}, search right half")
            low = mid + 1

        # Move left
        else:
            steps.append(f"→ {nums_sorted[mid]} > {target}, search left half")
            high = mid - 1

        steps.append("")  # add an empty line for spacing
        step += 1

    steps.append(f"→ {target} not found in the list.")
    return False, None, steps, nums_sorted

def run_search(array_str, target):
    """
    Called when the user clicks the 'Run Search' button.
    1. Parses the input list
    2. Converts target to integer
    3. Runs binary search
    4. Formats all messages for UI output
    """
    try:
        # parse list input
        nums = parse_list(array_str)

        # parse target value
        i = int(target)

        # run the binary search algorithm
        found, index, steps, nums_sorted = binary_search_steps(nums, i)

        # prepare summary text
        summary = []
        summary.append(f"Original list: {nums}")
        summary.append(f"Sorted list: {nums_sorted}")
        summary.append(f"Target: {i}")

        if found:
            summary.append(f"Result: Found at index {index}")
        else:
            summary.append(f"Result: Not found")

        return "\n".join(summary), "\n".join(steps)

    except Exception as e:
        # Catch any unexpected error and show it in the UI
        return "Error", f"{type(e).__name__}: {e}"

with gr.Blocks() as demo:
    gr.Markdown("# 🔍 Binary Search Visualizer\nEnter a list and a target number.")

    # User inputs
    input_array = gr.Textbox(
        label="Input Array (comma separated)",
        placeholder="Example: 5, 3, 9, 1, 7",
    )
    input_target = gr.Number(label="Target Number", precision=0)

    # Run button
    btn = gr.Button("Run Search")

    # Outputs
    output_summary = gr.Textbox(label="Result Summary")
    output_steps = gr.Textbox(label="Detailed Steps", lines=18)

    # Event
    btn.click(run_search, [input_array, input_target], [output_summary, output_steps])
    
if __name__ == "__main__":
    demo.launch()

