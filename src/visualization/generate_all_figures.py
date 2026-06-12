from score_distribution import ScoreDistribution
from hallucination_charts import HallucinationCharts
from benchmark_dashboard import BenchmarkDashboard

ScoreDistribution().generate()

HallucinationCharts().generate()

dashboard = BenchmarkDashboard()

dashboard.generate()

dashboard.domain_performance()

print(
    "All benchmark figures generated successfully."
)