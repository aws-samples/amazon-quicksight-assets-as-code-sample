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

	def add_calculated_field(self, calculated_field):
		self.calculated_fields.append(calculated_field.compile())

	def add_calculated_fields(self, calculated_field_list):
		for calculated_field in calculated_field_list:
			self.add_calculated_field(calculated_field)

	def add_parameter(self, parameter):
		self.parameter_declarations.append(parameter.compile())

	def add_parameters(self, parameter_list):
		for parameter in parameter_list:
			self.add_parameter(parameter)

	def add_filter_group(self, filter_group):
		self.filter_groups.append(filter_group.compile())

	def add_filter_groups(self, filter_group_list):
		for filter_group in filter_group_list:
			self.add_filter_group(filter_group)

	def set_analysis_default(self):
		self.analysis_defaults = {

				"DefaultNewSheetConfiguration": {
					"InteractiveLayoutConfiguration": {
						"FreeForm": {
							"CanvasSizeOptions": {
								"ScreenCanvasSizeOptions": {
									"OptimizedViewPortWidth": "1600px"
								}
							}
						}
						# "Grid": {
						# 	"CanvasSizeOptions": {
						# 		"ScreenCanvasSizeOptions": {
						# 			"ResizeOption": "FIXED",
						# 			"OptimizedViewPortWidth": "1600px"
						# 		}
						# 	}
						# }
					},
					"PaginatedLayoutConfiguration": {

					},
					"SheetContentType": "INTERACTIVE"
				}
			}
	
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
		self.id = sheet_id
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

	def add_filter_control(self, filter_control):
		self.filter_controls.append(filter_control.compile())

	def add_filter_controls(self, filter_control_list):
		for filter_control in filter_control_list:
			self.add_filter_control(filter_control)

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
				"ElementType": element.element_type,
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

	def set_grid_layout(self, resize_option = "", view_port_width = ""):
		self.layout = {
				"Configuration": {
					"GridLayout": {
						"Elements": [],
						"CanvasSizeOptions": {
							"ScreenCanvasSizeOptions":{
								"ResizeOption": resize_option,
								"OptimizedViewPortWidth": view_port_width
							}
						}
					}
				}
			}
	
	def add_grid_layout_element(self, element,  x_length, y_length, x_position = "", y_position = ""):
		self.layout["Configuration"]["GridLayout"]["Elements"].append(clean_dict({
				"ElementId": element.id,
				"ElementType": element.element_type,
				"ColumnSpan": x_length,
				"RowSpan": y_length,
				"ColumnIndex": x_position,
				"RowIndex": y_position
			}))

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
			"SheetId": self.id,
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

### CALCULATED FIELDS ###
class CalculatedField():
	def __init__(self, data_set_identifier, expression, name):
		self.data_set_identifier = data_set_identifier
		self.expression = expression
		self.name = name

	def compile(self):
		self.json = {
			"DataSetIdentifier": self.data_set_identifier,
			"Expression": self.expression,
			"Name": self.name
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
	def set_dynamic_default_value(self, column_name, data_set_identifier):
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
		self.id = parameter_control_id
		self.element_type = "PARAMETER_CONTROL"
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
				"ParameterControlId": self.id,
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
				"ParameterControlId": self.id,
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
				"ParameterControlId": self.id,
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
				"ParameterControlId": self.id,
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
				"ParameterControlId": self.id,
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
				"ParameterControlId": self.id,
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


### FILTER GROUP ###
class FilterGroup():
	def __init__(self,cross_dataset, filter_group_id):
		self.id = filter_group_id
		self.cross_dataset = cross_dataset
		self.filters = []
		self.sheet_visual_scoping_configurations = []
		self.status = ""

	def add_filter(self, filter):
		self.filters.append(filter.compile())

	def add_filters(self, filter_list):
		for filter in filter_list:
			self.add_filter(filter)

	def add_scope_configuration(self, scope, sheet_id, visual_ids = []):
		self.sheet_visual_scoping_configurations.append({
			"Scope": scope,
			"SheetId": sheet_id,
			"VisualIds": visual_ids
		})
	
	def set_status(self, status):
		self.status = status

	def compile(self):
		self.json = {
			"CrossDataset": self.cross_dataset,
			"FilterGroupId": self.id,
			"Filters": self.filters,
			"ScopeConfiguration": {
				"SelectedSheets": {
					"SheetVisualScopingConfigurations": self.sheet_visual_scoping_configurations
					}
				},
			"Status": self.status
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
			"CustomFilterConfiguration": {
				"MatchOperator": match_operator,
				"NullOption": null_option,
				"CategoryValue": category_value,
				"ParameterName": parameter_name,
				"SelectAllOptions": select_all_options
			}
		}

	def add_custom_filter_list_configuration(self, match_operator, null_option, category_values = [], select_all_options = ""):
		self.configuration = {
			"CustomFilterListConfiguration": {
				"MatchOperator": match_operator,
				"NullOption": null_option,
				"CategoryValues": category_values,
				"SelectAllOptions": select_all_options
			}
		}

	def add_filter_list_configuration(self, match_operator, category_values = [], select_all_options = ""):
		self.configuration = clean_dict({
			"FilterListConfiguration": {
				"MatchOperator": match_operator,
				"CategoryValues": category_values,
				"SelectAllOptions": select_all_options
			}
		})

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
class NumericEqualityFilter(Filter):
	def __init__(self, filter_id, column_name, data_set_identifier, match_operator, null_option):
		Filter.__init__(self, filter_id, column_name, data_set_identifier)
		
		self.match_operator = match_operator
		self.null_option = null_option
		self.select_all_options = ""
		self.value = ""
		self.parameter_name = ""
	
	def set_value(self, value):
		self.value = value

	def compile(self):
		self.json = {
			"NumericEqualityFilter": {
				"FilterId": self.filter_id,
				"Column": {
					"DataSetIdentifier": self.data_set_identifier,
					"ColumnName": self.column_name
				},
				"MatchOperator": self.match_operator,
				"NullOption": self.null_option,
				"AggregationFunction": {
					"CategoricalAggrecationFunction": "",
					"DateAggregationFunction": "",
					"NumericalAggregationFunction": {
						"PercentileAggregation": {
							"PercentileValue": ""
						},
						"SimpleNumericalAggregation": ""
					}

				},
				"ParameterName": self.parameter_name,
				"SelectAllOptions": self.select_all_options,
				"Value": self.value
			}
		}
		return clean_dict(self.json)
class TimeRangeFilter(Filter):
	def __init__(self, filter_id, column_name, data_set_identifier, null_option):
		Filter.__init__(self, filter_id, column_name, data_set_identifier)
		
		self.amount = ""
		self.granularity = ""
		self.status = ""
		self.include_maximum = ""
		self.include_minimum = ""
		self.max_value_parameter = ""
		self.min_value_parameter = ""
		self.time_granularity = ""

		self.null_option = null_option
	
	def add_min_value_parameter(self, min_value_parameter):
		self.min_value_parameter = min_value_parameter

	def compile(self):
		self.json = {
			"TimeRangeFilter": {
				"FilterId": self.filter_id,
				"Column": {
					"DataSetIdentifier": self.data_set_identifier,
					"ColumnName": self.column_name
				},
				"NullOption": self.null_option,
				"ExcludePeriodConfiguration": {
					"Amount": self.amount,
					"Granularity": self.granularity,
					"Status": self.status
				},
				"IncludeMaximum": self.include_maximum,
				"IncludeMinimum": self.include_minimum,
				"RangeMaximumValue": {},
				"RangeMinimumValue": {
					"Parameter": self.min_value_parameter
				},
				"TimeGranularity": self.time_granularity
			}
		}
		return clean_dict(self.json)


### FILTER CONTROLS ###
class FilterControl():
	def __init__(self, filter_control_id, source_filter_id, title):
		# ID of filter control
		self.id = filter_control_id
		self.element_type = "FILTER_CONTROL"
		# Name of source filter
		self.source_filter_id = source_filter_id
		# Title of filter control
		self.title = title

		self.custom_label = ""
		self.font_color = ""
		self.font_decoration = ""
		self.font_size = ""
		self.font_style = ""
		self.font_weight = ""
		self.title_options_visibility = ""
class FilterDateTimePickerControl(FilterControl):
	def __init__(self, filter_control_id, source_filter_id, title):
		FilterControl.__init__(self, filter_control_id, source_filter_id, title)

		self.type = ""
		self.date_time_format = ""
	
	def set_date_time_format(self, date_time_format):
		self.date_time_format = date_time_format

	def compile(self):
		self.json = {
			"DateTimePicker": {
				"FilterControlId": self.id,
				"SourceFilterId": self.source_filter_id,
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
							},
						"Visibility": self.title_options_visibility
						},
					}
				},
				"Type": self.type
			}
		}

		return clean_dict(self.json)

### VISUALS ###
class Visual():
	def __init__(self, visual_id):
		# Available in All Visuals
		self.id = visual_id
		self.element_type = "VISUAL"
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

	def add_categorical_dimension_field(self, column_name, data_set_identifier):
		self.category.append(
			{
				"CategoricalDimensionField": {
					"FieldId": column_name,
					"Column": {
						"ColumnName": column_name,
						"DataSetIdentifier": data_set_identifier
					}
				}
			})

	def add_date_dimension_field(self, column_name, data_set_identifier, date_granularity = "", date_time_format = "", null_string = ""):
		self.category.append(clean_dict(
			{
				"DateDimensionField": {
					"FieldId": column_name,
					"Column": {
						"ColumnName": column_name,
						"DataSetIdentifier": data_set_identifier
					},
					"DateGranularity": date_granularity,
					"FormatConfiguration": {
						"DateTimeFormat": date_time_format,
						"NullValueFormatConfiguration": {
							"NullString": null_string
						},
						"NumericFormatConfiguration": {}
					}
				}
			}))

	def add_numerical_dimension_field(self, column_name, data_set_identifier, hierarchy_id = ""):
		self.category.append(
			{
				"NumericalDimensionField": {
					"FieldId": column_name,
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
	def add_numerical_measure_field(self, column_name, data_set_identifier, aggregation_function = None, 
				 currency_decimal_places = '', currency_number_scale = '', currency_prefix = '', currency_suffix = '',currency_symbol = '',
				 percentage_suffix = ''):
		self.values.append(clean_dict(
				{
					"NumericalMeasureField": {
						"FieldId": column_name,
						"Column": {
							"ColumnName": column_name,
							"DataSetIdentifier": data_set_identifier
						},
						"AggregationFunction": {
							"SimpleNumericalAggregation": aggregation_function
						},
						"FormatConfiguration": {
							"FormatConfiguration": {
								"CurrencyDisplayFormatConfiguration": {
									"DecimalPlacesConfiguration": {
										"DecimalPlaces": currency_decimal_places
									},
									"NumberScale": currency_number_scale,
									"Prefix": currency_prefix,
									"Suffix": currency_suffix,
									"Symbol": currency_symbol
								},
								"NumberDisplayFormatConfiguration": {},
								"PercentageDisplayFormatConfiguration": {
									"Suffix": percentage_suffix
								}
							}
						}
					}
				}))
	
	def add_filter_action(self,custom_action_id, action_name, trigger, status = "ENABLED", selected_field_options = "", selected_fields = [], target_visual_options = [], target_visuals = []):
		self.actions.append({
			"ActionOperations": [
				{
					"FilterOperation":{
						"SelectedFieldsConfiguration": {
							"SelectedFieldOptions": selected_field_options,
							"SelectedFields": selected_fields
						},
						"TargetVisualsConfiguration": {
							"SameSheetTargetVisualConfiguration": {
								"TargetVisualOptions": target_visual_options,
								"TargetVisuals": target_visuals
							}
						}
					}
				}
			],
			"CustomActionId": custom_action_id,
			"Name": action_name,
			"Trigger": trigger,
			"Status": status
		})
class BarChartVisual(Visual):
	def __init__(self, visual_id):
		Visual.__init__(self, visual_id)

		self.bars_arrangement = ""
		self.orientation = ""

		self.axis_line_visibility = ""
		self.axis_offset = ""
		self.grid_line_visibility = ""
		self.scroll_bar_visibility = ""
		self.visible_range_from = ""
		self.visible_range_to = ""

	def set_bars_arrangement(self, bars_arrangement):
		self.bars_arrangement = bars_arrangement

	def set_orientation(self, orientation):
		self.orientation = orientation

	def set_scroll_bar_visibility(self, scroll_bar_visibility):
		self.scroll_bar_visibility = scroll_bar_visibility

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
					"Orientation": self.orientation,
					"CategoryAxis": {
						"AxisLineVisibility": self.axis_line_visibility,
						"AxisOffset": self.axis_offset,
						"GridLineVisbility": self.grid_line_visibility,
						"ScrollbarOptions": {
							"Visibility": self.scroll_bar_visibility,
							"VisibleRange": {
								"PercentRange": {
									"From": self.visible_range_from,
									"To": self.visible_range_to
								}
							}
						}
					}
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
		self.axis_line_visibility = ""
		self.axis_offset = ""
		self.grid_line_visibility = ""
		self.scroll_bar_visibility = ""
		self.visible_range_from = ""
		self.visible_range_to = ""
	
	def set_type(self, type):
		self.type = type

	def set_scroll_bar_visibility(self, scroll_bar_visibility):
		self.scroll_bar_visibility = scroll_bar_visibility

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
					"XAxisDisplayOptions": {
						"AxisLineVisibility": self.axis_line_visibility,
						"AxisOffset": self.axis_offset,
						"GridLineVisbility": self.grid_line_visibility,
						"ScrollbarOptions": {
							"Visibility": self.scroll_bar_visibility,
							"VisibleRange": {
								"PercentRange": {
									"From": self.visible_range_from,
									"To": self.visible_range_to
								}
							}
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
		self.field_sort = []
	
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

	def add_field_sort(self,field_id, direction):
		self.field_sort.append({
			"FieldSort": {
				"Direction": direction,
				"FieldId": field_id
			}
		})

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
					},
					"SortConfiguration": {
						"RowSort": self.field_sort
					}
				},
				"ConditionalFormatting": {
					"ConditionalFormattingOptions": {
						"Cell": {
							"FieldId": "",
							"TextFormat": {
								"BackgroundColor": {
									"Gradient": {
										"Color": {
											"Stops": []
										},
										"Expression": ""
									},
									"Solid": {
										"Color": "",
										"Expression": ""
									}
								},
								"Icon": {
									"CustomCondition": {
										"Color": "",
										"Expression": "",
										"IconOptions": {
											"Icon": "",
											"UnicodeIcon": ""
										},
										"DisplayConfiguration": {
											"IconDisplayOption": ""
										}
									}
								},
								"TextColor": {
									"Gradient": {
										"Color": {
											"Stops": []
										},
										"Expression": ""
									},
									"Solid": {
										"Color": "",
										"Expression": ""
									}
								}
							}
						},
						"Row": {
							"BackgroundColor": {
								"Gradient": {
									"Color": {
										"Stops": []
									},
									"Expression": ""
								},
								"Solid": {
									"Color": "",
									"Expression": ""
								}
							},
							"TextColor": {
								"Gradient": {
									"Color": {
										"Stops": []
									},
									"Expression": ""
								},
								"Solid": {
									"Color": "",
									"Expression": ""
								}
							}
						}
					}
				},
				"Title": self.title,
				"subtitle": self.subtitle
			}
		}

		return clean_dict(self.json)
class PivotTableVisual(Visual):
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

	def add_calculated_measure_field(self, expression, field_id):
		self.values.append(
				{
					"CalculatedMeasureField": {
						"FieldId": field_id,
						"Expression": expression
					}
				})
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
def clean_dict(input):
    if type(input) is dict:
        return dict((key, clean_dict(value)) for key, value in input.items() if (value or value == 0) and clean_dict(value) not in [{},[],""])
    elif type(input) is list:
        return [clean_dict(item) for item in input if (item or item == 0) and clean_dict(item) not in [{},[],""]]
    else:
	    if input or input == 0:
		    return input

###################################################################
### This where we are going to create dashboard objects as code ###
###################################################################

# Analysis
analysis_1 = Analysis('752669751623','analysis1','Assets as Code - Sample Analysis')

# Analysis Definition
analysis_definition = Definition([{"DataSetArn":"arn:aws:quicksight:us-east-1:752669751623:dataset/fddb4301-4e9d-458c-bb61-ad68ec168e24","Identifier":"SaaS-Sales.csv"}])
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
file = analysis_1.compile()
print(file)

with open("create-analysis.json", "w") as outfile:
	outfile.write(file)