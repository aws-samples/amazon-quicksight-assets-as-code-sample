## QuickSight Assets-as-Code

Amazon QuickSight Assets-as-Code allow customers and partners to treat BI resources as code assets that sit outside of the QuickSight platform. This unlocks a number of capabilities, including but not limited to use cases such as programmatic dashboard creation, version control, BI workfload migration, and much more.

Currently, these APIs (*DescribeAnalysisDefinition, DescribeTemplateDefinition, DescribeDashboardDefinition*) allow developers to manage all supported charts and visual components in JSON format.

With complex dashboards with many resources, however, navigating through nested JSON code can be difficult to update and maintain. This code sample takes Assets-as-Code a step further and demonstrates way to define dashboard resources as python objects.

*Note: This code sample is not comprehensive of all QuickSight resources and visual types, and simply showcases potential capabilities.*
## Example

# Visuals
For example, to create a new Line Chart object, you can simply call the below line of code.
```
linechart_1 = LineChartVisual(visual_id = 'linechart1')
```
You can also configure additional settings by calling class-specific functions, such as adding a field or a title for your visual.
```
linechart_1.set_type('LINE')

linechart_1.add_date_dimension_field('Order Date','SaaS-Sales.csv', date_granularity = "MONTH")
```

Once you are done defining your resources, the code sample will package all of your resources into a single JSON structure that is acceptable by QuickSight.

# Sheets
Similarly, you can create sheets and further configure the sheet.
```
sheet_1 = Sheet('sheet1', name = "AnyCompany Sales")
sheet_1.set_title("AnyCompany Sales")
sheet_1.set_grid_layout("FIXED", "1600px")
```
You can add objects to your sheet, and even specify the layout and size of your visuals.
```
sheet_1.add_grid_layout_element(linechart_1, 13, 10, 0, 10)
sheet_1.add_grid_layout_element(table_1, 13, 10, 13, 10)
sheet_1.add_grid_layout_element(parameter_date_control_1, 7, 3, 26, 0)
```

## How it works

The repo contains three main constructs - 1) **quicksight_assets_class.py**, 2) **create-analysis.py**, and 3) **asset-definition.json**.

1. **quicksight_assets_class.py**
    - This is the python code that wraps QuickSight JSON objects into Python Classes.
2. **create-analysis.py**
    - This is the part where you define dashboard objects you want to create, including parameters, calculated fields, visuals, etc.
    - Once you define all the resources, the code will also generate a final JSON file that contains the analysis definition.
3. **asset-definition.json**
    - This is the JSON file that will be used in the create-analysis or update-analysis APIs to either create a new analysis or update an existing analysis.

You can call the API using the AWS CLI as noted below, or use AWS SDKs in your programming language of choice.
```
aws quicksight update-analysis --cli-input-json file://asset-definition.json --region us-east-1 --profile [your-aws-profile-here]
```
## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

