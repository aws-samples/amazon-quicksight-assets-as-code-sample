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

	def add_parameter(self, parameter):
		self.parameter_declarations.append(parameter.compile())

	def add_parameters(self, parameter_list):
		for parameter in parameter_list:
			self.add_parameter(parameter)

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

### SHEET ###
class Sheet():
	def __init__(self, sheet_id, name):
		self.sheet_id = sheet_id
		self.name = name
		self.title = ""
		self.description = ""
		self.visuals = []
		self.filter_controls = []
		self.parameter_controls = []
		self.layout = {}
		self.content_type = ""
		self.text_boxes = []

	def add_visual(self, visual):
		self.visuals.append(visual.compile())

	def add_visuals(self, visual_list):
		for visual in visual_list:
			self.add_visual(visual)

	def add_parameter_control(self, parameter_control):
		self.parameter_controls.append(parameter_control.compile())

	def add_parameter_controls(self, parameter_control_list):
		for parameter_control in parameter_control_list:
			self.add_parameter_control(parameter_control)

	def add_text_box(self, text_box):
		self.text_boxes.append(text_box.compile())
	
	def add_text_boxes(self, text_box_list):
		for text_box in text_box_list:
			self.add_text_box(text_box)

	def set_content_type(self, content_type):
		self.content_type = content_type

	def set_name(self, name):
		self.name = name

	def set_title(self, title):
		self.title = title
	
	def set_description(self, description):
		self.description = description

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
			"ContentType": self.content_type,
			"Description": self.description,
			"FilterControls": self.filter_controls,
			"Layouts": [clean_dict(self.layout)],
			"Name": self.name,
			"ParameterControls": self.parameter_controls,
			"SheetControlLayouts": [],
			"TextBoxes": self.text_boxes,
			"Title": self.title,
			"Visuals": self.visuals		
		}

		return clean_dict(self.json)

### LAYOUT ###
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


### PARAMETERS ###
class Parameter():
	def __init__(self, name):
		self.name = name

		self.custom_value = ""
		self.value_when_unset_option = ""
		self.default_value = {}

	def set_static_default_value(self, static_default_value):
		self.default_value = {
			"StaticValues": [static_default_value]
		}

	# TODO: NEEDS UPDATE
	def set_dynamic_default_value(self, column_name, data_set_identifier ):
		self.default_value = {
			"DynamicValue": {
				"DefaultValueColumn": {
					"ColumnName": column_name,
					"DataSetIdentifier": data_set_identifier
				},
				"GroupNameColumn": "",
				"UserNameColumn": ""
			}
		}

	def set_value_when_unset(self, custom_value = "", value_when_unset_option=""):
		# Value depends on parameter type
		self.custom_value = custom_value
		# RECOMMENDED_VALUE | NULL
		self.value_when_unset_option = value_when_unset_option

class DateTimeParameter(Parameter):
	def __init__(self, name):
		Parameter.__init__(self, name)

		self.time_granularity = ""
	
	def set_rolling_date_default_value(self, expression, data_set_identifier = ""):
		self.default_value = {
			"RollingDate": {
				"Expression": expression,
				"DataSetIdentifier": data_set_identifier
			}
		}

	# YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND
	def set_time_granularity(self, time_granularity):
		self.time_granularity = time_granularity

	def compile(self):
		self.json = {
			"DateTimeParameterDeclaration": {
				"Name": self.name,
				"DefaultValues": self.default_value,
				"TimeGranularity": self.time_granularity,
				"ValueWhenUnset": {
					"CustomValue": self.custom_value,
					"ValueWhenUnsetOption": self.value_when_unset_option
				}
			}
		}

		return clean_dict(self.json)

class DecimalParameter(Parameter):
	def __init__(self, name, parameter_value_type):
		Parameter.__init__(self, name)

		# MULTI_VALUED | SINGLE_VALUED
		self.parameter_value_type = parameter_value_type

	def compile(self):
		self.json = {
			"DecimalParameterDeclaration": {
				"Name": self.name,
				"DefaultValues": self.default_value,
				"ParameterValueType": self.parameter_value_type,
				"ValueWhenUnset": {
					"CustomValue": self.custom_value,
					"ValueWhenUnsetOption": self.value_when_unset_option
				}
			}
		}

		return clean_dict(self.json)

class IntegerParameter(Parameter):
	def __init__(self, name, parameter_value_type):
		Parameter.__init__(self, name)

		# MULTI_VALUED | SINGLE_VALUED
		self.parameter_value_type = parameter_value_type

	def compile(self):
		self.json = {
			"IntegerParameterDeclaration": {
				"Name": self.name,
				"DefaultValues": self.default_value,
				"ParameterValueType": self.parameter_value_type,
				"ValueWhenUnset": {
					"CustomValue": self.custom_value,
					"ValueWhenUnsetOption": self.value_when_unset_option
				}
			}
		}
		return clean_dict(self.json)

class StringParameter(Parameter):
	def __init__(self, name, parameter_value_type):
		Parameter.__init__(self, name)

		# MULTI_VALUED | SINGLE_VALUED
		self.parameter_value_type = parameter_value_type

	def compile(self):
		self.json = {
			"IntegerParameterDeclaration": {
				"Name": self.name,
				"DefaultValues": self.default_value,
				"ParameterValueType": self.parameter_value_type,
				"ValueWhenUnset": {
					"CustomValue": self.custom_value,
					"ValueWhenUnsetOption": self.value_when_unset_option
				}
			}
		}
		return clean_dict(self.json)


### PARAMETER CONTROLS ###
class ParameterControl():
	def __init__(self, parameter_control_id, parameter_name, title):
		# ID of parameter control
		self.parameter_control_id = parameter_control_id
		# Name of source parameter
		self.source_parameter_name = parameter_name
		# Title of parameter control
		self.title = title

		self.custom_label = ""
		self.font_color = ""
		self.font_decoration = ""
		self.font_size = ""
		self.font_style = ""
		self.font_weight = ""
		self.title_options_visibility = ""

	def set_title_font(self, font_color = "", font_decoration = "", font_size = "", font_style = "", font_weight = ""):
		self.font_color = font_color
		self.font_decoration = font_decoration
		self.font_size = font_size
		self.font_style = font_style
		self.font_weight = font_weight
class ParameterDateTimePickerControl(ParameterControl):
	def __init__(self, parameter_control_id, parameter, title):
		ParameterControl.__init__(self, parameter_control_id, parameter, title)

		self.date_time_format = ""

	def compile(self):
		self.json = {
			"DateTimePicker": {
				"ParameterControlId": self.parameter_control_id,
				"SourceParameterName": self.source_parameter_name,
				"Title": self.title,
				"DisplayOptions": {
					"DateTimeFormat": self.date_time_format,
					"TitleOptions": {
						"CustomLabel": self.custom_label,
						"FontConfiguration": {
							"FontColor": self.font_color,
							"FontDecoration": self.font_decoration,
							"FontSize": {
								"Relative": self.font_size
							},
							"FontStyle": self.font_style,
							"FontWeight": {
								"Name": self.font_weight
							}
						},
						"Visibility": self.title_options_visibility						
					}
				}
			}
		}
		return clean_dict(self.json)
class ParameterDropDownControl(ParameterControl):
	def __init__(self, parameter_control_id, parameter, title):
		ParameterControl.__init__(self, parameter_control_id, parameter, title)
		self.select_all_options_visibility = ""
		self.type = ""
		self.column_name = ""
		self.data_set_identifier = ""
		self.values = []

	def compile(self):
		self.json = {
			"Dropdown": {
				"ParameterControlId": self.parameter_control_id,
				"SourceParameterName": self.source_parameter_name,
				"Title": self.title,
				"DisplayOptions": {
					"SelectAllOptions": {
						"Visibility": self.select_all_options_visibility
					},
					"TitleOptions": {
						"CustomLabel": self.custom_label,
						"FontConfiguration": {
							"FontColor": self.font_color,
							"FontDecoration": self.font_decoration,
							"FontSize": {
								"Relative": self.font_size
							},
							"FontStyle": self.font_style,
							"FontWeight": {
								"Name": self.font_weight
							}
						},
						"Visibility": self.title_options_visibility
					}
				},
				"Type": self.type,
				"SelectableValues": {
					"LinkToDataSetColumn": {
						"ColumnName": self.column_name,
						"DataSetIdentifier": self.data_set_identifier					
					},
					"Values": self.values
				}
			}
		}
		return clean_dict(self.json)
class ParameterListControl(ParameterControl):
	def __init__(self, parameter_control_id, parameter, title):
		ParameterControl.__init__(self, parameter_control_id, parameter, title)
		self.search_options_visibility = ""
		self.select_all_options_visibility = ""
		self.column_name = ""
		self.data_set_identifier = ""
		self.values = []
		self.type = ""

	def compile(self):
		self.json = {
			"Dropdown": {
				"ParameterControlId": self.parameter_control_id,
				"SourceParameterName": self.source_parameter_name,
				"Title": self.title,
				"CascadingControlConfiguration": {					

				},
				"DisplayOptions": {
					"SearchOptions": {
						"Visibility": self.search_options_visibility
					},
					"SelectAllOptions": {
						"Visibility": self.select_all_options_visibility
					},
					"TitleOptions": {
						"CustomLabel": self.custom_label,
						"FontConfiguration": {
							"FontColor": self.font_color,
							"FontDecoration": self.font_decoration,
							"FontSize": {
								"Relative": self.font_size
							},
							"FontStyle": self.font_style,
							"FontWeight": {
								"Name": self.font_weight
							}
						},
						"Visibility": self.title_options_visibility
					}
				},
				"SelectableValues": {
					"LinkToDataSetColumn": {
						"ColumnName": self.column_name,
						"DataSetIdentifier": self.data_set_identifier					
					},
					"Values": self.values
				},
				"Type": self.type
			}
		}
		return clean_dict(self.json)
class ParameterSliderControl(ParameterControl):
	def __init__(self, parameter_control_id, parameter, title, maximum_value, minimum_value, step_size):
		ParameterControl.__init__(self, parameter_control_id, parameter, title)
		self.maximum_value = maximum_value
		self.minimum_value = minimum_value
		self.step_size = step_size

	def compile(self):
		self.json = {
			"Slider": {
				"MaximumValue": self.maximum_value,
				"MinimumValue": self.minimum_value,
				"ParameterControlId": self.parameter_control_id,
				"SourceParameterName": self.source_parameter_name,
				"StepSize": self.step_size,
				"Title": self.title,
				"DisplayOptions": {
					"TitleOptions": {
						"CustomLabel": self.custom_label,
						"FontConfiguration": {
							"FontColor": self.font_color,
							"FontDecoration": self.font_decoration,
							"FontSize": {
								"Relative": self.font_size
							},
							"FontStyle": self.font_style,
							"FontWeight": {
								"Name": self.font_weight
							}
						},
						"Visibility": self.title_options_visibility
					}
				}
			}
		}
		return clean_dict(self.json)
class ParameterTextAreaControl(ParameterControl):
	def __init__(self, parameter_control_id, parameter, title):
		ParameterControl.__init__(self, parameter_control_id, parameter, title)
		self.delimiter = ""
		self.placeholder_options_visibility = ""

	def compile(self):
		self.json = {
			"TextArea": {
				"ParameterControlId": self.parameter_control_id,
				"SourceParameterName": self.source_parameter_name,
				"Title": self.title,
				"Delimiter": self.delimiter,
				"DisplayOptions": {
					"PlaceholderOptions": {
						"Visibility": self.placeholder_options_visibility
					},
					"TitleOptions": {
						"CustomLabel": self.custom_label,
						"FontConfiguration": {
							"FontColor": self.font_color,
							"FontDecoration": self.font_decoration,
							"FontSize": {
								"Relative": self.font_size
							},
							"FontStyle": self.font_style,
							"FontWeight": {
								"Name": self.font_weight
							}
						},
						"Visibility": self.title_options_visibility
					}
				}
			}
		}
		return clean_dict(self.json)
class ParameterTextFieldControl(ParameterControl):
	def __init__(self, parameter_control_id, parameter, title):
		ParameterControl.__init__(self, parameter_control_id, parameter, title)
		self.placeholder_options_visibility = ""

	def compile(self):
		self.json = {
			"TextArea": {
				"ParameterControlId": self.parameter_control_id,
				"SourceParameterName": self.source_parameter_name,
				"Title": self.title,
				"DisplayOptions": {
					"PlaceholderOptions": {
						"Visibility": self.placeholder_options_visibility
					},
					"TitleOptions": {
						"CustomLabel": self.custom_label,
						"FontConfiguration": {
							"FontColor": self.font_color,
							"FontDecoration": self.font_decoration,
							"FontSize": {
								"Relative": self.font_size
							},
							"FontStyle": self.font_style,
							"FontWeight": {
								"Name": self.font_weight
							}
						},
						"Visibility": self.title_options_visibility
					}
				}
			}
		}
		return clean_dict(self.json)


### FILTERS ###
class Filter():
	def __init__(self, filter_id, column_name, data_set_identifier):

		self.filter_id = filter_id
		self.column_name = column_name
		self.data_set_identifier = data_set_identifier

class CategoryFilter(Filter):
	def __init__(self, filter_id, column_name, data_set_identifier):
		Filter.__init__(self, filter_id, column_name, data_set_identifier)
		
		self.configuration = {}
	
	def add_custom_filter_configuration(self, match_operator, null_option, category_value = "", parameter_name = "", select_all_options = ""):
		self.configuration = {
			"Configuration": {
				"CustomFilterConfiguration": {
					"MatchOperator": match_operator,
					"NullOption": null_option,
					"CategoryValue": category_value,
					"ParameterName": parameter_name,
					"SelectAllOptions": select_all_options
				}
			}
		}

	def add_custom_filter_list_configuration(self, match_operator, null_option, category_values = [], select_all_options = ""):
		self.configuration = {
			"Configuration": {
				"CustomFilterConfiguration": {
					"MatchOperator": match_operator,
					"NullOption": null_option,
					"CategoryValues": category_values,
					"SelectAllOptions": select_all_options
				}
			}
		}

	def add_filter_list_configuration(self, match_operator, category_values = [], select_all_options = ""):
		self.configuration = {
			"Configuration": {
				"CustomFilterConfiguration": {
					"MatchOperator": match_operator,
					"CategoryValues": category_values,
					"SelectAllOptions": select_all_options
				}
			}
		}

	def compile(self):
		self.json = {
			"CategoryFilter": {
				"FilterId": self.filter_id,
				"Column": {
					"DataSetIdentifier": self.data_set_identifier,
					"ColumnName": self.column_name
				},
				"Configuration": self.configuration
			}
		}
		return clean_dict(self.json)

### VISUALS ###
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

### TEXTBOX ###
class TextBox():
	def __init__(self, text_box_id, content):
		self.text_box_id = text_box_id
		self.content = content

	def compile(self):
		self.json = {
			"SheetTextBoxId": self.text_box_id,
			"Content": self.content
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

# Analysis
analysis_1 = Analysis('752669751623','test12333','test-analysis-123334')

# Analysis Definition
analysis_definition = Definition([{"DataSetArn":"arn:aws:quicksight:us-east-1:752669751623:dataset/4152f9d8-c75c-4d0f-805c-ebd12fcaf77d","Identifier":"AnyCompany Data Set (Company).xlsx"}])

# Parameters
date_parameter_1 = DateTimeParameter("Date")
date_parameter_1.set_static_default_value("2017/01/01")
date_parameter_1.set_time_granularity("DAY")

integer_parameter_1 = IntegerParameter("digit","MULTI_VALUED")

# Sheet
sheet_1 = Sheet('sheetid1234', name = "sales")
sheet_1.set_title("Sales Dashboard")
sheet_1.set_description("This is a sheet about sales")

# Parameter Controls
parameter_date_control_1 = ParameterDateTimePickerControl("id1234", date_parameter_1.name, "Date")
parameter_date_control_1.set_title_font(font_decoration="UNDERLINE")
parameter_drop_down_control_1 = ParameterDropDownControl("112312", integer_parameter_1.name, "Number")

# Visuals
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

# # Text Boxes (ERROR)
# text_box_1 = TextBox("asdklh", "")

# sheet_1.set_freeform_layout()
# sheet_1.add_freeform_layout_element(barchart_1, "300px", "300px", "8px", "8px")

sheet_2 = Sheet('sheetid321', name = "costs")
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

# First, add visuals and parameter controls to the sheet they belong to
sheet_1.add_visuals([barchart_1,barchart_2])
sheet_1.add_parameter_controls([parameter_date_control_1, parameter_drop_down_control_1])
# sheet_1.add_text_boxes([text_box_1])

sheet_2.add_visuals([barchart_3,linechart_3, table_1])

# Next, add all sheets to the analysis definition object
analysis_definition.add_sheets([sheet_1,sheet_2])
analysis_definition.add_parameters([date_parameter_1, integer_parameter_1])

# Next, add the analysis definition object to the analysis object
analysis_1.add_definition(analysis_definition)

# Finally, compile the analysis into a single JSON object
file = analysis_1.compile()
print(file)

with open("create-analysis.json", "w") as outfile:
	outfile.write(file)

