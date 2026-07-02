# Load Testing Report

Tool Used:

k6

## Configuration

- Virtual Users: 20
- Duration: 1 Minute

## Results

| Metric | Result |
|---------|--------|
| Requests | 396 |
| Success Rate | 100% |
| Failed Requests | 0 |
| Avg Response Time | 1.79 s |
| Max Response Time | 3.34 s |
| Throughput | 6.29 req/sec |

## Observation

The application handled concurrent requests successfully without failures.

Performance can be improved by:

- Larger EC2 Instance
- Nginx Reverse Proxy
- Application Load Balancer
- Auto Scaling