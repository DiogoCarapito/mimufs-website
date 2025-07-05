def gradient_text_logo_svg(text, output_path="logo.svg"):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" height="120">
      <defs>
        <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" style="stop-color:#FF6A00;stop-opacity:1" />
          <stop offset="100%" style="stop-color:#FFD800;stop-opacity:1" />
        </linearGradient>
      </defs>
      <text x="10" y="90" font-family="Arial, sans-serif" font-size="80" font-weight="bold" fill="url(#grad)">{text}</text>
    </svg>"""
    with open(output_path, "w") as f:
        f.write(svg)

    # save as png aslo


if __name__ == "__main__":
    gradient_text_logo_svg("mimufs", "assets/mimufs.svg")
    print("Logo generated as mimufs.svg")
