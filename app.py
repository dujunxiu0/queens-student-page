import gradio as gr


def parse_array(array_str):
    try:
        parts = array_str.split(",")
        nums = []
        for p in parts:
            p = p.strip()
            if p:
                nums.append(int(p))
        return nums
    except:
        raise ValueError("Please enter only integers separated by commas.")


def binary_search_steps(nums, target):
    nums_sorted = sorted(nums)
    low = 0
    high = len(nums_sorted) - 1
    steps = []
    step = 1

    while low <= high:
        mid = (low + high) // 2
        steps.append(
            f"Step {step}: low={low}, high={high}, mid={mid}, value={nums_sorted[mid]}"
        )

        if nums_sorted[mid] == target:
            steps.append(f"→ Found {target} at index {mid}")
            return True, mid, steps, nums_sorted

        elif nums_sorted[mid] < target:
            steps.append(f"→ {nums_sorted[mid]} < {target}, search RIGHT half")
            low = mid + 1

        else:
            steps.append(f"→ {nums_sorted[mid]} > {target}, search LEFT half")
            high = mid - 1

        steps.append("")
        step += 1

    steps.append(f"→ {target} not found in the list.")
    return False, None, steps, nums_sorted


def run_search(array_str, target):
    try:
        nums = parse_array(array_str)
    except ValueError as e:
        return "❌ Error", str(e)

    found, index, steps, nums_sorted = binary_search_steps(nums, target)

    summary = []
    summary.append(f"Original list: {nums}")
    summary.append(f"Sorted list: {nums_sorted}")
    summary.append(f"Target: {target}")

    if found:
        summary.append(f"✅ Result: Found at index {index}")
    else:
        summary.append(f"❌ Result: Not found")

    return "\n".join(summary), "\n".join(steps)


with gr.Blocks() as demo:
    gr.Markdown("# 🔍 Binary Search Visualizer\nEnter a list and a target number.")

    input_array = gr.Textbox(
        label="Input Array (comma separated)",
        placeholder="Example: 5, 3, 9, 1, 7",
    )
    input_target = gr.Number(label="Target Number", precision=0)

    btn = gr.Button("Run Search")

    output_summary = gr.Textbox(label="Result Summary")
    output_steps = gr.Textbox(label="Detailed Steps", lines=18)

    btn.click(run_search, [input_array, input_target], [output_summary, output_steps])

if __name__ == "__main__":
    demo.launch()

