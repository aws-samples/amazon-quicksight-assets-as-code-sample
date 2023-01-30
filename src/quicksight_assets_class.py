import json

class Analysis():
	def __init__(self, aws_account_id, analysis_id, analysis_name):
		self.aws_account_id = aws_account_id
		self.analysis_id = analysis_id
		self.analysis_name = analysis_name
		self.definition = {}
		self.parameters = {}
		self.permissions = {}
		self.source_entity = {}
		self.tags = []
		self.theme_arn = ""

	def add_tags(self, tag_key, tag_value):
		self.tags.append({tag_key,tag_value})

	def add_definition(self, definition):
		self.definition = definition.compile()

	def set_theme_arn(self, theme_arn):
		self.theme_arn = theme_arn

	def compile(self):
		self.json = {
			"AwsAccountId": self.aws_account_id,
		    "AnalysisId": self.analysis_id,
		    "Name": self.analysis_name,
		    "Definition": self.definition,
		    "Parameters": self.parameters,
		    "Permissions": self.permissions,
		    "SourceEntity": self.source_entity,
		    "Tags": self.tags,
		    "ThemeArn": self.theme_arn
		}

		return json.dumps(clean_dict(self.json),indent = 6)


class Definition():
	def __init__(self, data_set_definition):
		self.data_set_definition = data_set_definition
		self.sheets = []
		self.calculated_fields = []
		self.column_configurations = []
		self.filter_groups = []
		self.parameter_declarations = []
		self.analysis_defaults = {}

	def add_sheet(self, sheet):
		self.sheets.append(sheet.compile())

	def add_sheets(self, sheet_list):
		for sheet in sheet_list:
			self.add_sheet(sheet)

	def compile(self):
		self.json = {
		    "DataSetIdentifierDeclarations": self.data_set_definition,
		    "AnalysisDefaults": self.analysis_defaults,
		    "CalculatedFields": self.calculated_fields,
		    "ColumnConfigurations": self.column_configurations,
		    "FilterGroups": self.filter_groups,
		    "ParameterDeclarations": self.parameter_declarations,
		    "Sheets": self.sheets
		}

		return clean_dict(self.json)


class Sheet():
	def __init__(self, sheet_id, name, title = ""):
		self.sheet_id = sheet_id
		self.name = name
		self.title = title
		self.visuals = []
		self.layout = {}
		self.content_type = "content_type"

	def add_visual(self, visual):
		self.visuals.append(visual.compile())

	def add_visuals(self, visual_list):
		for visual in visual_list:
			self.add_visual(visual)

	def set_content_type(self, content_type):
		self.json["ContentType"] = content_type

	def set_name(self, name):
		self.json["Name"] = name

	def set_freeform_layout(self):
		self.layout = {
			"Configuration": {
				"FreeFormLayout": {
					"Elements": [],
					"CanvasSizeOptions": {
						"ScreenCanvasSizeOptions":{
							"OptimizedViewPortWidth": ""
						}
					}
				}
			}
		}
	def add_freeform_layout_element(self, element, height, width, x_axis_location, y_axis_location, background_style = {}, border_style = {}, loading_animation = {}, rendering_rules = {}, selected_border_style = {}, visibility = ""):
		self.layout["Configuration"]["FreeFormLayout"]["Elements"].append(clean_dict({
				"ElementId": element.id,
				"ElementType": element.type,
				"Height": height,
				"Width": width,
				"XAxisLocation": x_axis_location,
				"YAxisLocation": y_axis_location,
				"BorderStyle": border_style,
				"LoadingAnimation": loading_animation,
				"RenderingRules": rendering_rules,
				"SelectedBorderStyle": selected_border_style,
				"Visbility": visibility
			}))

	def set_grid_layout(self):
		self.layout = {
				"Configuration": {
					"GridLayout": {
						"Elements": [],
						"CanvasSizeOptions": {
							"ScreenCanvasSizeOptions":{
								"ResizeOption": "",
								"OptimizedViewPortWidth": ""
							}
						}
					}
				}
			}

	def set_section_based_layout(self):
		self.layout = {
				"Configuration": {
					"SectionBasedLayout": {
						"BodySections": [],
						"CanvasSizeOptions": {
							"ScreenCanvasSizeOptions":{
								"PaperCanvasSizeOptions": {
									"PaperMargin":{
										"Bottom": "",
										"Left": "",
										"Right": "",
										"Top": ""
									},
									"PaperOrientation": "",
									"PaperSize": ""
								}
							}
						}
					}
				}
			}

	def compile(self):
		self.json = {
			"SheetId": self.sheet_id,
			"Name": self.name,
			"Title": self.title,
			"Visuals": self.visuals,
			"Layouts": [clean_dict(self.layout)]
		}

		return clean_dict(self.json)

class FreeFormLayout():
	def __init__(self):
		self.elements = []
		self.canvas_size_options = ""

	def add_element(self, element, height, width, x_axis_location, y_axis_location, background_style = {}, border_style = {}, loading_animation = {}, rendering_rules = {}, selected_border_style = {}, visibility = ""):
		self.elements.append(clean_dict({
				"ElementId": element.id,
				"ElementType": element.type,
				"Height": height,
				"Width": width,
				"XAxisLocation": x_axis_location,
				"YAxisLocation": y_axis_location,
				"BorderStyle": border_style,
				"LoadingAnimation": loading_animation,
				"RenderingRules": rendering_rules,
				"SelectedBorderStyle": selected_border_style,
				"Visbility": visibility
			}))

	def set_canvas_size_options():
		pass

	def compile(self):
		self.json = {
			"Configuration": {
				"FreeFormLayout": {
					"Elements": self.elements,
					"CanvasSizeOptions": {
						"ScreenCanvasSizeOptions":{
							"OptimizedViewPortWidth": self.canvas_size_options
						}
					}
				}
			}
		}
		return clean_dict(self.json)

class Visual():
	def __init__(self, visual_id):
		# Available in All Visuals
		self.id = visual_id
		self.type = "VISUAL"
		self.actions = []
		self.title = {}
		self.subtitle = {}

		# Available in BarChart, LineChart, etc
		self.column_hierarchies = []

		# Available in TableVisual, etc.
		self.conditional_formatting = {}


		self.category = []
		self.values = []
		self.colors = []
		self.small_multiples = []

		self.group_by = []

	def add_title(self, visibility, text_format, text):
		self.title = {
			"Visibility": visibility,
			"FormatText": {
				text_format: text
			}
		}

	def add_subtitle(self, visibility, text_format, text):
		self.subtitle = {
			"Visibility": visibility,
			"FormatText": {
				text_format: text
			}
		}

	def add_action(self):
		pass

	def add_categorical_dimension_field(self, column_name, data_set_identifier):
		self.category.append(
			{
				"CategoricalDimensionField": {
					"FieldId": data_set_identifier + column_name,
					"Column": {
						"ColumnName": column_name,
						"DataSetIdentifier": data_set_identifier
					}
				}
			})

	def add_date_dimension_field(self, column_name, data_set_identifier, date_granularity = "", date_time_format = "", null_string = ""):
		self.category.append(
			{
				"DateDimensionField": {
					"FieldId": data_set_identifier + column_name,
					"Column": {
						"ColumnName": column_name,
						"DataSetIdentifier": data_set_identifier
					},
					"DateGranularity": date_granularity,
					"DateTimeFormatConfiguration": {
						"DateTimeFormat": date_time_format,
						"NullValueFormatConfiguration": {
							"NullString": null_string
						},
						"NumericFormatConfiguration": ""
					}
				}
			})

	def add_numerical_dimension_field(self, column_name, data_set_identifier, hierarchy_id = ""):
		self.category.append(
			{
				"NumericalDimensionField": {
					"FieldId": data_set_identifier + column_name,
					"Column": {
						"ColumnName": column_name,
						"DataSetIdentifier": data_set_identifier
					},
					"NumberFormatConfiguration": {
						"CurrencyDisplayFormatConfiguration": {},
						"NumberDisplayFormatConfiguration": {},
						"PercentageDisplayFormatConfiguration": {}
					},
					"HierarchyId": hierarchy_id
				}
			})
	def add_numerical_measure_field(self, column_name, data_set_identifier, aggregation_function = None):
		self.values.append(
				{
					"NumericalMeasureField": {
						"FieldId": data_set_identifier + column_name,
						"Column": {
							"ColumnName": column_name,
							"DataSetIdentifier": data_set_identifier
						},
						"AggregationFunction": {
							"SimpleNumericalAggregation": aggregation_function
						}
					}
				})

class BarChartVisual(Visual):
	def __init__(self, visual_id):
		Visual.__init__(self, visual_id)

		self.bars_arrangement = ""
		self.orientation = ""

	def set_bars_arrangement(self, bars_arrangement):
		self.bars_arrangement = bars_arrangement

	def set_orientation(self, orientation):
		self.orientation = orientation

	def compile(self):
		self.json = {
			"BarChartVisual":{
				"VisualId": self.id,
				"Actions": self.actions,
				"ChartConfiguration": {
					"FieldWells": {
						"BarChartAggregatedFieldWells": {
							"Category": self.category,
							"Values": self.values,
							"Colors": self.colors,
							"SmallMultiples": self.small_multiples
						}
					},
					"BarsArrangement": self.bars_arrangement,
					"Orientation": self.orientation
				},
				"ColumnHierarchies": self.column_hierarchies,
				"Title": self.title,
				"Subtitle": self.subtitle

			}
		}

		return clean_dict(self.json)

class LineChartVisual(Visual):
	def __init__(self, visual_id):
		Visual.__init__(self,visual_id)

		self.type = ""
	
	def set_type(self, type):
		self.type = type

	def compile(self):
		self.json = {
			"LineChartVisual":{
				"VisualId": self.id,
				"ChartConfiguration": {
					"FieldWells": {
						"LineChartAggregatedFieldWells": {
							"Category": self.category,
							"Values": self.values,
							"Colors": self.colors,
							"SmallMultiples": self.small_multiples
						}
					},
					"Type": self.type

				},
				"Title": self.title,
				"subtitle": self.subtitle
			}
		}
		
		visual_clean = clean_dict(self.json)

		return visual_clean


class TableVisual(Visual):
	def __init__(self, visual_id):
		Visual.__init__(self,visual_id)

		self.unaggregated_values = []
	
	def add_unaggregated_date_time_value(self, column_name, data_set_identifier, date_time_format="", null_string=""):
		self.unaggregated_values.append(
			{
				"UnaggregatedField": {
					"FieldId": data_set_identifier + column_name,
					"Column": {
						"ColumnName": column_name,
						"DataSetIdentifier": data_set_identifier
						},
					"FormatConfiguration": {
						"DateTimeFormatConfiguration": {
							"DateTimeFormat": date_time_format,
							"NullValueFormatConfiguration": {
								"NullString": null_string
							},
							"NumericFormatConfiguration": ""
						}
					}
				}
			})

	def add_group_by(self, column_name, data_set_identifier):
		self.add_categorical_dimension_field(column_name, data_set_identifier)

	def compile(self):
		self.json = {
			"TableVisual":{
				"VisualId": self.id,
				"ChartConfiguration": {
					"FieldWells": {
						"TableAggregatedFieldWells": {
							"GroupBy": self.category,
							"Values": self.values
						},
						"TableUnaggregatedFieldWells": {
							"Values": self.unaggregated_values
						}
					}
				},
				"Title": self.title,
				"subtitle": self.subtitle
			}
		}

		return clean_dict(self.json)

# Recursive function to remove parameters with empty values from dictionary object
def clean_dict(input_dict):
	new_dict = {}
	for key, value in input_dict.items():
		if isinstance(value, dict):
			value = clean_dict(value)
		if value not in ["", [], {}, [{}]]:
			new_dict[key] = value
	return new_dict

analysis_1 = Analysis('752669751623','test12333','test-analysis-123334')

analysis_definition = Definition([{"DataSetArn":"arn:aws:quicksight:us-east-1:752669751623:dataset/4152f9d8-c75c-4d0f-805c-ebd12fcaf77d","Identifier":"AnyCompany Data Set (Company).xlsx"}])

sheet_1 = Sheet('sheetid1234', name = "sheet 1")

barchart_1 = BarChartVisual('123456789')
barchart_1.set_bars_arrangement('CLUSTERED')
barchart_1.set_orientation('VERTICAL')
barchart_1.add_categorical_dimension_field('Company','AnyCompany Data Set (Company).xlsx')
barchart_1.add_numerical_measure_field('Order #','AnyCompany Data Set (Company).xlsx','SUM')
barchart_1.add_title("VISIBLE","PlainText","This is my title")
barchart_1.add_subtitle("VISIBLE","PlainText","This is my subtitle")

barchart_2 = BarChartVisual('232424')
barchart_2.set_bars_arrangement('STACKED')
barchart_2.set_orientation('HORIZONTAL')
barchart_2.add_categorical_dimension_field('Company','AnyCompany Data Set (Company).xlsx')
barchart_2.add_numerical_measure_field('Order #','AnyCompany Data Set (Company).xlsx','AVERAGE')

sheet_1.set_freeform_layout()
sheet_1.add_freeform_layout_element(barchart_1, "300px", "300px", "8px", "8px")

sheet_2 = Sheet('sheetid321', name = "sheet 123")
barchart_3 = BarChartVisual('23409')
barchart_3.set_bars_arrangement('STACKED')
barchart_3.set_orientation('HORIZONTAL')
barchart_3.add_categorical_dimension_field('Company','AnyCompany Data Set (Company).xlsx')
barchart_3.add_numerical_measure_field('Order #','AnyCompany Data Set (Company).xlsx','SUM')

linechart_3 = LineChartVisual('234239')
linechart_3.set_type('LINE')
linechart_3.add_categorical_dimension_field('Company','AnyCompany Data Set (Company).xlsx')
linechart_3.add_numerical_measure_field('Order #','AnyCompany Data Set (Company).xlsx','SUM')

table_1 = TableVisual('iolewhtli')
table_1.add_group_by('Company','AnyCompany Data Set (Company).xlsx')

# First, add visuals to the sheet they belong to
sheet_1.add_visuals([barchart_1,barchart_2])
sheet_2.add_visuals([barchart_3,linechart_3, table_1])

# Next, add all sheets to the analysis definition object
analysis_definition.add_sheets([sheet_1,sheet_2])

# Next, add the analysis definition object to the analysis object
analysis_1.add_definition(analysis_definition)

# Finally, compile the analysis into a single JSON object
file = analysis_1.compile()
print(file)

with open("create-analysis-2.json", "w") as outfile:
	outfile.write(file)

