class Analysis():
	def __init__(self, aws_account_id, analysis_id, analysis_name):
		# The ID of the AWS account where you are creating an analysis.
		self.aws_account_id = aws_account_id

		# The ID for the analysis that you're creating. This ID displays in the URL of the analysis.
		self.analysis_id = analysis_id

		# A descriptive name for the analysis that you're creating. 
		# This name displays for the analysis in the Amazon QuickSight console.
		self.analysis_name = analysis_name

		# A definition is the data model of all features in a Dashboard, Template, or Analysis.
		#Either a SourceEntity or a Definition must be provided in order for the request to be valid.
		self.definition = {}

		# The parameter names and override values that you want to use.
		self.parameters = {}

		# A structure that describes the principals and the resource-level permissions on an analysis. 
		# You can use the Permissions structure to grant permissions by providing a list of 
		# AWS Identity and Access Management (IAM) action information for each principal listed by Amazon Resource Name (ARN).
		self.permissions = []

		# A source entity to use for the analysis that you're creating. 
		# This metadata structure contains details that describe a source template and one or more datasets.
		self.source_entity = {}

		# Contains a map of the key-value pairs for the resource tag or tags assigned to the analysis.
		self.tags = []

		# The ARN for the theme to apply to the analysis that you're creating.
		self.theme_arn = ""

	def add_tag(self, tag_key, tag_value):
		self.tags.append({"Key": tag_key,"Value": tag_value})

	def add_permission(self, actions, principal):
		self.permissions.append({"Actions": actions, "Principal": principal})

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

		return clean_dict(self.json)
	
class Definition():
	def __init__(self, data_set_definition):
		# An array of dataset identifier declarations. 
		# This mapping allows the usage of dataset identifiers instead of dataset ARNs throughout analysis sub-structures.
		self.data_set_definition = data_set_definition

		# The configuration for default analysis settings.
		self.analysis_defaults = {}		

		# An array of calculated field definitions for the analysis.
		self.calculated_fields = []

		# An array of analysis-level column configurations. 
		# Column configurations can be used to set default formatting for a column to be used throughout an analysis.
		self.column_configurations = []

		# Filter definitions for an analysis.
		self.filter_groups = []

		#An array of parameter declarations for an analysis.
		self.parameter_declarations = []

		# An array of sheet definitions for an analysis. 
		# Each SheetDefinition provides detailed information about a sheet within this analysis.
		self.sheets = []

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

		return self.json

### SHEET ###
class Sheet():
	def __init__(self, sheet_id, name):
		# The unique identifier of a sheet.
		self.id = sheet_id

		# The layout content type of the sheet. Choose one of the following options:
		# Valid Values: PAGINATED | INTERACTIVE
		self.content_type = ""	

		# A description of the sheet.
		self.description = ""

		# The list of filter controls that are on a sheet.
		self.filter_controls = []

		# Layouts define how the components of a sheet are arranged.
		self.layout = {}

		# The name of the sheet. 
		# This name is displayed on the sheet's tab in the Amazon QuickSight console.
		self.name = name

		# The list of parameter controls that are on a sheet.
		self.parameter_controls = []

		# The control layouts of the sheet.
		self.sheet_control_layouts = []

		# The text boxes that are on a sheet.
		self.text_boxes = []		

		# The title of the sheet.
		self.title = ""

		# A list of the visuals that are on a sheet.
		# Visual placement is determined by the layout of the sheet.
		self.visuals = []

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
		self.layout["Configuration"]["FreeFormLayout"]["Elements"].append({
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
			})

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
		self.layout["Configuration"]["GridLayout"]["Elements"].append({
				"ElementId": element.id,
				"ElementType": element.element_type,
				"ColumnSpan": x_length,
				"RowSpan": y_length,
				"ColumnIndex": x_position,
				"RowIndex": y_position
			})

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
			"Layouts": [self.layout],
			"Name": self.name,
			"ParameterControls": self.parameter_controls,
			"SheetControlLayouts": [],
			"TextBoxes": self.text_boxes,
			"Title": self.title,
			"Visuals": self.visuals		
		}

		return self.json

### CALCULATED FIELDS ###
class CalculatedField():
	def __init__(self, data_set_identifier, expression, name):
		# The data set that is used in this calculated field.
		self.data_set_identifier = data_set_identifier

		# The expression of the calculated field.
		self.expression = expression

		# The name of the calculated field.
		self.name = name

	def compile(self):
		self.json = {
			"DataSetIdentifier": self.data_set_identifier,
			"Expression": self.expression,
			"Name": self.name
		}

		return self.json
	
### PARAMETERS ###
class Parameter():
	def __init__(self, name):
		# The name of the parameter that is being declared.
		self.name = name

		# The default values of a parameter. 
		# If the parameter is a single-value parameter, a maximum of one default value can be provided.
		self.default_value = {}

		# A custom value that's used when the value of a parameter isn't set.
		self.custom_value = ""

		# The built-in options for default values. The value can be one of the following:
		# RECOMMENDED_VALUE | NULL
		self.value_when_unset_option = ""

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

		# The level of time precision that is used to aggregate DateTime values.
		# Valid Values: YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND
		self.time_granularity = ""
	
	def set_rolling_date_default_value(self, expression, data_set_identifier = ""):
		self.default_value = {
			"RollingDate": {
				"Expression": expression,
				"DataSetIdentifier": data_set_identifier
			}
		}

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

		return self.json
class DecimalParameter(Parameter):
	def __init__(self, name, parameter_value_type):
		Parameter.__init__(self, name)

		# The value type determines whether the parameter is a single-value or multi-value parameter.
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

		return self.json
class IntegerParameter(Parameter):
	def __init__(self, name, parameter_value_type):
		Parameter.__init__(self, name)

		# The value type determines whether the parameter is a single-value or multi-value parameter.
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
		return self.json
class StringParameter(Parameter):
	def __init__(self, name, parameter_value_type):
		Parameter.__init__(self, name)

		# The value type determines whether the parameter is a single-value or multi-value parameter.
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
		return self.json

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
		return self.json
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
		return self.json
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
		return self.json
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
		return self.json
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
		return self.json
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
		return self.json

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

		return self.json

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
		self.configuration = {
			"FilterListConfiguration": {
				"MatchOperator": match_operator,
				"CategoryValues": category_values,
				"SelectAllOptions": select_all_options
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
		return self.json
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
		return self.json
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
		return self.json

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

		return self.json

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
		self.category.append(
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
			})

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
		self.values.append(
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
				})
	
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

		return self.json
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

		return self.json
class TableVisual(Visual):
	def __init__(self, visual_id):
		Visual.__init__(self,visual_id)

		self.unaggregated_values = []
		self.field_sort = []
		self.inline_visualizations = []
		self.conditional_formatting_options = []

		self.cell_background_color = ""
		self.header_background_color = ""

		self.cell_border = {}
		self.header_border = {}
	
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

	def add_field_sort(self, field_id, direction):
		self.field_sort.append({
			"FieldSort": {
				"Direction": direction,
				"FieldId": field_id
			}
		})

	def set_cell_border_type(self, border_type, color = "", style="", thickness=""):

		border_options = {}
		border_options[border_type] = { 
				"Color": color,
				"Style": style,
				"Thickness": thickness
		}

		if border_type == "UniformBorder":
			self.cell_border = border_options
		else:
			self.cell_border = {
				"SideSpecificBorder": border_options
			}
	
	def set_header_border_type(self, border_type, color = "", style="", thickness=""):
		border_options = {}
		border_options[border_type] = { 
				"Color": color,
				"Style": style,
				"Thickness": thickness
		}

		if border_type == "UniformBorder":
			self.header_border = border_options
		else:
			self.header_border = {
				"SideSpecificBorder": border_options
			}

	def add_inline_visualization(self, field_id, negative_color = "", positive_color = ""):
		self.inline_visualizations.append({
			"DataBars": {
				"FieldId": field_id,
				"NegativeColor": negative_color,
				"PositiveColor": positive_color
			}
		})

	def add_icon_conditional_formatting(self, field_id, expression, icon = "", unicode_icon = "", color = "", icon_display_option = ""):
		self.conditional_formatting_options.append({
			"Cell": {
				"FieldId": field_id,
				"TextFormat": {
					"Icon": {
						"CustomCondition": {
							"Expression": expression,
							"IconOptions": {
								"Icon": icon,
								"UnicodeIcon": unicode_icon
							},
							"Color": color,
							"DisplayConfiguration": {
								"IconDisplayOption": icon_display_option
							}
						},
						# "IconSet": {
						# 	"Expression": icon_set_expression,
						# 	# PLUS_MINUS | CHECK_X | THREE_COLOR_ARROW | THREE_GRAY_ARROW | CARET_UP_MINUS_DOWN | THREE_SHAPE | 
						# 	# THREE_CIRCLE | FLAGS | BARS | FOUR_COLOR_ARROW | FOUR_GRAY_ARROW
						# 	"IconSetType": icon_set_type
						# }
					}
				}
			}
		}
		)

	def add_gradient_text_conditional_formatting(self, field_id, expression, gradient_stops = []):
		self.conditional_formatting_options.append({
			"Cell": {
				"FieldId": field_id,
				"TextFormat": {
					"TextColor": {
						"Gradient": {
							"Expression": expression,
							"Color": {
								"Stops": gradient_stops
							}
						}
					}
				}
			}
		}
		)		

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
					},
					"TableInlineVisualizations": self.inline_visualizations,
					"TableOptions": {
						"CellStyle": {
							"BackgroundColor": self.cell_background_color,
							"Border": self.cell_border
						},
						"HeaderStyle": {
							"BackgroundColor": self.header_background_color,
							"Border": self.header_border
						}
					}
				},
				"ConditionalFormatting": {
					"ConditionalFormattingOptions": self.conditional_formatting_options
				},
				"Title": self.title,
				"subtitle": self.subtitle
			}
		}

		return self.json
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

		return self.json

# Recursive function to remove parameters with empty values from dictionary object
def clean_dict(input):
    if type(input) is dict:
        return dict((key, clean_dict(value)) for key, value in input.items() if (value or value == 0) and clean_dict(value) not in [{},[],""])
    elif type(input) is list:
        return [clean_dict(item) for item in input if (item or item == 0) and clean_dict(item) not in [{},[],""]]
    else:
	    if input or input == 0:
		    return input