from quicksight_assets_class import *

###################################################################
### This where we are going to create dashboard objects as code ###
###################################################################

def main():
	# Analysis
	analysis_1 = Analysis('<your-aws-account-id>','analysis1','Assets as Code - Sample Analysis')

	# Analysis Definition
	analysis_definition = Definition([{"DataSetArn":"<your-dataset-arn>","Identifier":"SaaS-Sales.csv"}])
	analysis_definition.set_analysis_default()

	# Parameters
	date_parameter_1 = DateTimeParameter("Date")
	date_parameter_1.set_static_default_value("2017/01/01")
	date_parameter_1.set_time_granularity("DAY")

	integer_parameter_1 = IntegerParameter("digit","MULTI_VALUED")

	# Filters
	product_filter = CategoryFilter("asdgasg", "Product", 'SaaS-Sales.csv')
	product_filter.add_filter_list_configuration('CONTAINS',['Alchemy','Big Ol Database', 'Data Smasher'])

	date_filter = TimeRangeFilter("time_range_filter_1", "Order Date", 'SaaS-Sales.csv', "ALL_VALUES")
	date_filter.add_min_value_parameter(date_parameter_1.name)

	# Filter Control

	# Calculated Fields
	calculated_field_1 = CalculatedField("SaaS-Sales.csv", "{Sales} - {Profit}", "Cost")

	# Sheet
	sheet_1 = Sheet('sheet1', name = "AnyCompany Sales")
	sheet_1.set_title("AnyCompany Sales")
	sheet_1.set_description("This dashboard shows YTD Sales on AnyCompany Products. All the assets in this dashboard (Visuals, Parameters, Filters, Actions, etc.) were programmatically created using assets-as-code.")
	sheet_1.set_grid_layout("FIXED", "1600px")

	sheet_2 = Sheet('sheet2', name = "costs")
	sheet_2.set_freeform_layout()


	# Parameter Controls
	parameter_date_control_1 = ParameterDateTimePickerControl("id1234", date_parameter_1.name, "Date")
	parameter_date_control_1.set_title_font(font_decoration="UNDERLINE")

	# Visuals
	barchart_1 = BarChartVisual('barchart1')
	barchart_1.set_bars_arrangement('CLUSTERED')
	barchart_1.set_orientation('VERTICAL')
	barchart_1.add_categorical_dimension_field('Product','SaaS-Sales.csv')
	barchart_1.add_numerical_measure_field('Sales','SaaS-Sales.csv','SUM')
	barchart_1.add_title("VISIBLE","PlainText","Sum of Sales by Product")
	barchart_1.add_subtitle("VISIBLE","PlainText","Use this visual to drill down into specific products.")
	barchart_1.set_scroll_bar_visibility("HIDDEN")
	barchart_1.add_filter_action("quick_filter_action_1", "Quick Filter", "DATA_POINT_CLICK", selected_field_options = "ALL_FIELDS", target_visual_options= "ALL_VISUALS")

	barchart_2 = BarChartVisual('barchart2')
	barchart_2.set_bars_arrangement('STACKED')
	barchart_2.set_orientation('HORIZONTAL')
	barchart_2.add_categorical_dimension_field('Product','SaaS-Sales.csv')
	barchart_2.add_numerical_measure_field('Profit','SaaS-Sales.csv','AVERAGE')
	barchart_2.set_scroll_bar_visibility("HIDDEN")
	barchart_2.add_title("VISIBLE","PlainText","Average Profit by Product")


	linechart_1 = LineChartVisual('linechart1')
	linechart_1.set_type('LINE')
	linechart_1.add_date_dimension_field('Order Date','SaaS-Sales.csv', date_granularity = "MONTH")
	linechart_1.add_numerical_measure_field('Sales','SaaS-Sales.csv','SUM')
	linechart_1.add_numerical_measure_field('Profit','SaaS-Sales.csv','SUM')
	linechart_1.add_numerical_measure_field('Cost','SaaS-Sales.csv','SUM')
	linechart_1.add_title("VISIBLE","PlainText","Sales vs Profit over time")
	linechart_1.set_scroll_bar_visibility("HIDDEN")

	barchart_3 = BarChartVisual('barchart3')
	barchart_3.set_bars_arrangement('STACKED')
	barchart_3.set_orientation('HORIZONTAL')
	barchart_3.add_categorical_dimension_field('Product','SaaS-Sales.csv')
	barchart_3.add_numerical_measure_field('Sales','SaaS-Sales.csv','SUM')

	linechart_3 = LineChartVisual('linechart3')
	linechart_3.set_type('LINE')
	linechart_3.add_categorical_dimension_field('Product','SaaS-Sales.csv')
	linechart_3.add_numerical_measure_field('Sales','SaaS-Sales.csv','SUM')

	table_1 = TableVisual('table1')
	table_1.add_categorical_dimension_field('Product','SaaS-Sales.csv')
	table_1.add_numerical_measure_field('Sales','SaaS-Sales.csv','SUM', currency_symbol="USD")
	table_1.add_numerical_measure_field('Profit','SaaS-Sales.csv','SUM', currency_symbol="USD")
	table_1.add_numerical_measure_field('Quantity','SaaS-Sales.csv','SUM')
	table_1.add_numerical_measure_field('Discount','SaaS-Sales.csv','AVERAGE', percentage_suffix = '%')
	table_1.add_field_sort("Sales", "DESC")
	table_1.add_title("VISIBLE","PlainText","Product Metrics Table")


	# Filter Group
	filter_group_1 = FilterGroup("ALL_DATASETS", "filtergroup1")
	filter_group_1.add_scope_configuration("ALL_VISUALS", sheet_1.id)
	filter_group_1.add_filters([product_filter])
	filter_group_1.set_status("ENABLED")

	filter_group_2 = FilterGroup("ALL_DATASETS", "filtergroup2")
	filter_group_2.add_scope_configuration("ALL_VISUALS", sheet_1.id)
	filter_group_2.add_filters([date_filter])
	filter_group_2.set_status("ENABLED")

	# First, add all elements (visuals, parameter controls, action controls, etc) to the sheet they belong to
	sheet_1.add_visuals([barchart_1,barchart_2,linechart_1, table_1])
	sheet_1.add_parameter_controls([parameter_date_control_1])
	sheet_2.add_visuals([barchart_3,linechart_3])

	# Next, specify the layout of all the elements
	sheet_1.add_grid_layout_element(barchart_1, 13, 10, 0, 0)
	sheet_1.add_grid_layout_element(barchart_2, 13, 10, 13, 0)
	sheet_1.add_grid_layout_element(linechart_1, 13, 10, 0, 10)
	sheet_1.add_grid_layout_element(table_1, 13, 10, 13, 10)
	sheet_1.add_grid_layout_element(parameter_date_control_1, 7, 3, 26, 0)

	sheet_2.add_freeform_layout_element(linechart_3, "800px","600px","450px","0px")
	sheet_2.add_freeform_layout_element(barchart_3, "600px","600px","0px","800px")


	# Next, add all sheets to the analysis definition object
	analysis_definition.add_sheets([sheet_1,sheet_2])
	analysis_definition.add_parameters([date_parameter_1, integer_parameter_1])
	analysis_definition.add_filter_groups([filter_group_1, filter_group_2])
	analysis_definition.add_calculated_fields([calculated_field_1])

	# Next, add the analysis definition object to the analysis object
	analysis_1.add_definition(analysis_definition)

	# Finally, compile the analysis into a single JSON object
	file = json.dumps(analysis_1.compile(), indent=6)
	print(file)

	with open("asset_definition.json", "w") as outfile:
		outfile.write(file)

if __name__ == "__main__":
	main()