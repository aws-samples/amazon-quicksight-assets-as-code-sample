## QuickSight Assets-as-Code

Amazon QuickSight Assets-as-Code allow customers and partners to treat BI resources as code assets that sit outside of the QuickSight platform. This unlocks a number of capabilities, including but not limited to use cases such as programmatic dashboard creation, version control, BI workfload migration, and much more.

Currently, these APIs (DescribeAnalysisDefinition, DescribeTemplateDefinition, DescribeDashboardDefinition) allow developers to manage all supported charts and visual components in JSON format.

With complex dashboards with many resources, however, navigating through nested JSON code can be difficult to update and maintain. This code sample takes Assets-as-Code a step further and demonstrates way to define dashboard resources as python objects.

For example, to create a new Line Chart object, you can simply call the below line of code.
```
linechart_1 = LineChartVisual(visual_id = 'linechart1')
```
You can also configure additional settings by calling class-specific functions, such as adding a field or a title for your visual.
```
linechart_1.set_type('LINE')

linechart_1.add_date_dimension_field('Order Date','SaaS-Sales.csv', date_granularity = "MONTH")
```
Note: This code sample is not comprehensive of all QuickSight resources and visual types, and simply showcases potential capabilities.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

