# Quality Check for Purchase Order Line

## Introduction 🌐

This customization focuses on enhancing the quality check process for purchase order lines, as outlined in the specifications below. 💯

## Rationale ♻️

The objective is to streamline the purchase validation process by incorporating additional information, such as the quantity on hand, the price of the previous purchase, and the number of sales in the past 365 days.

## Specification ✍️

- **New Column: Sales in Last 365 Days**

  - Add a column next to the quantity on hand that displays the number of sales in the last 365 days.

- **Quality Checker Column**

  - Introduce a new column named 'Quality Checker' that compares several key metrics:

    - Quantity on hand
    - Required quantity
    - Quantity sold in the last 365 days

  - **Visual Indicators:**
    - Green: Indicates that everything is satisfactory.
    - Orange: Prompts further review.

## Usage

To run the project, execute the following command:

```py
    python odoo-bin -c run.conf
```

```py
    python odoo-bin -c run.conf -d odoo16-1 -u gse_purchase_qc --test-enable --test-file=gse_purchase_qc --stop-after-init
```

Implement a visual representation using these three colors to enhance the user experience and quickly communicate the status of the quality check process.

Feel free to explore and contribute to this branch to improve the efficiency and accuracy of the purchase order validation process. Your feedback and suggestions are highly appreciated! 🚀
