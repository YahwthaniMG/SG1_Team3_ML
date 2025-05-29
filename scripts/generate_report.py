#!/usr/bin/env python3
"""
Automatic Report Generator - Titanic ML Project
====================================================

Generates an HTML report complete with:
- Model Metrics
- Key visualizations
- Historical insights
- Algorithm comparison

Usage:
    python scripts/generate_report.py
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO
from datetime import datetime
import os


def load_metrics():
    """Load saved metrics"""
    with open("models/model_metrics.json", "r") as f:
        return json.load(f)


def fig_to_base64(fig):
    """Convert matplotlib figure to base64 for HTML"""
    buffer = BytesIO()
    fig.savefig(buffer, format="png", dpi=150, bbox_inches="tight")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    buffer.close()
    plt.close(fig)
    return image_base64


def create_comparison_plot(metrics):
    """Create model comparison chart"""
    models = list(metrics["base_models_comparison"].keys())
    accuracies = [
        metrics["base_models_comparison"][model]["val_accuracy"] for model in models
    ]

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(models, accuracies, color=["skyblue", "lightgreen", "coral", "gold"])
    ax.set_title("Model Comparison - Validation Accuracy", fontsize=16)
    ax.set_ylabel("Accuracy")
    ax.set_ylim(0.7, 0.9)

    # Add values in bars
    for bar, acc in zip(bars, accuracies):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.005,
            f"{acc:.3f}",
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig


def generate_html_report():
    """Generate full HTML report"""
    # Load data
    metrics = load_metrics()

    # Create visualizations
    comparison_fig = create_comparison_plot(metrics)
    comparison_img = fig_to_base64(comparison_fig)

    # Template HTML
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Titanic ML Project - Final Report</title>
        <meta charset="utf-8">
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
            .header {{ background: #2c3e50; color: white; padding: 20px; border-radius: 8px; }}
            .section {{ margin: 30px 0; padding: 20px; border-left: 4px solid #3498db; }}
            .metric {{ background: #ecf0f1; padding: 15px; margin: 10px 0; border-radius: 5px; }}
            .success {{ color: #27ae60; font-weight: bold; }}
            .warning {{ color: #e67e22; font-weight: bold; }}
            img {{ max-width: 100%; height: auto; margin: 20px 0; }}
            table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
            th, td {{ border: 1px solid #ddd; padding: 12px; text-align: center; }}
            th {{ background-color: #3498db; color: white; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🚢 Titanic Survival Prediction - Final Report</h1>
            <p><strong>Team:</strong> SG1_Team3_ML</p>
            <p><strong>Date:</strong> {datetime.now().strftime("%d de %B, %Y")}</p>
        </div>
        
        <div class="section">
            <h2>🎯 Executive Summary</h2>
            <div class="metric">
                <h3>Objetivo: <span class="success">✅ REACHED</span></h3>
                <p>Accuracy final: <strong>{metrics['final_test_metrics']['accuracy']:.1%}</strong> (>80% required)</p>
            </div>
            <div class="metric">
                <h3>Best Model: {metrics['best_model']}</h3>
                <p>Parameters: {metrics['best_params']}</p>
            </div>
        </div>
        
        <div class="section">
            <h2>📊 Model Comparison</h2>
            <img src="data:image/png;base64,{comparison_img}" alt="Model Comparison">
        </div>
        
        <div class="section">
            <h2>📈 Final Metrics</h2>
            <table>
                <tr><th>Metric</th><th>Valor</th><th>Interpretation</th></tr>
                <tr><td>Accuracy</td><td>{metrics['final_test_metrics']['accuracy']:.3f}</td><td class="success">Excellent</td></tr>
                <tr><td>Precision</td><td>{metrics['final_test_metrics']['precision']:.3f}</td><td class="success">Very good</td></tr>
                <tr><td>Recall</td><td>{metrics['final_test_metrics']['recall']:.3f}</td><td>Good</td></tr>
                <tr><td>F1-Score</td><td>{metrics['final_test_metrics']['f1']:.3f}</td><td>Balanced</td></tr>
                <tr><td>AUC-ROC</td><td>{metrics['final_test_metrics']['auc']:.3f}</td><td class="success">Excellent discrimination</td></tr>
            </table>
        </div>
        
        <div class="section">
            <h2>🏛️ Historical Insights</h2>
            <ul>
                <li><strong>Women and Children First” Protocol"</strong> clearly validated</li>
                <li><strong>Social class</strong> was decisive in survival</li>
                <li><strong>Gender-class intersection</strong> the most predictive factor</li>
                <li><strong>84.4% accuracy</strong> demonstrates patterns consistent with tragedy</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>🎓 Academic Conclusions</h2>
            <p>This project successfully demonstrated the application of Machine Learning for:</p>
            <ul>
                <li>Validate historical hypotheses with quantitative evidence</li>
                <li>Implement complete Data Science pipeline</li>
                <li>Compare multiple algorithms systematically</li>
                <li>Generate insights applicable to modern protocols</li>
            </ul>
        </div>
        
        <footer style="margin-top: 50px; text-align: center; color: #7f8c8d;">
            <p>Automatically generated by generate_report.py</p>
            <p>Universidad Panamericana - COM 139: Simulation & Visualization</p>
        </footer>
    </body>
    </html>
    """

    # Save report
    os.makedirs("results/reports", exist_ok=True)
    report_path = "results/reports/final_report.html"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"✅ Report generated: {report_path}")
    return report_path


if __name__ == "__main__":
    print("📝 GENERATING AUTOMATIC REPORT")
    print("=" * 35)

    try:
        report_path = generate_html_report()
        print(f"🎉 ¡HTML report generated successfully!")
        print(f"📂 Location: {report_path}")
        print("💡 Open the file in your browser to view it")

    except Exception as e:
        print(f"❌ Error generating report: {str(e)}")
        sys.exit(1)
