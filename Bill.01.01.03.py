import sqlite3  
import flet as ft

def obtener_todos_los_productos():
    conn = sqlite3.connect("tienda_ecuador.db")
    cursor = conn.cursor()

    cursor.execute("SELECT codigo, nombre, precio_unidad, iva FROM inventario")
    productos = cursor.fetchall()

    conn.close()
    return productos

def obtener_datos_producto_por_codigo(codigo):
    conn = sqlite3.connect("tienda_ecuador.db")
    cursor = conn.cursor()

    cursor.execute("SELECT nombre, precio_unidad, iva FROM inventario WHERE codigo=?", (codigo,))
    producto = cursor.fetchone()

    conn.close()
    return producto




#!Crear la tabla6
Data_table=ft.DataTable(
    width=1100,
    columns=[
        ft.DataColumn(ft.Text("ID"),),
        ft.DataColumn(ft.Text("Nombre")),
        ft.DataColumn(ft.Text("Precio Unidad")),
        ft.DataColumn(ft.Text("IVA")),
    ],
    rows=[

    ]

    )
    #!Agregar los productos a la tabla de la base de datos
max_productos = 0
productos_disponibles = obtener_todos_los_productos()
for producto in productos_disponibles:
    max_productos= max_productos +1
    codigo, nombre, precio_unidad, iva = producto
    #print(f"Código: {codigo}, Nombre: {nombre}, Precio: {precio_unidad}, IVA: {iva}%")
    Data_table.rows.append(ft.DataRow(
        cells=[
            ft.DataCell(ft.Text(codigo)),
            ft.DataCell(ft.Text(nombre)),
            ft.DataCell(ft.Text(precio_unidad)),
            ft.DataCell(ft.Text(iva)),

            ],
        ),)
class Task(ft.UserControl):
    
    def __init__(self, task_name, task_delete):
        super().__init__()
        self.task_name = task_name
        self.task_delete = task_delete

    def build(self):

        
        self.display_task = ft.Text(self.task_name)
        producto = obtener_datos_producto_por_codigo(self.display_task.value)
        nombre, precio, iva = producto   
        print(f"Nombre: {nombre}, Precio: {precio}, IVA: {iva}%")    
        print(self.display_task.value)
        

        self.display_view = ft.Row(
            alignment=ft.alignment.top_center,
            vertical_alignment=ft.MainAxisAlignment.START,
            controls=[
                self.display_task,
                ft.Container(content=ft.Text(nombre,color=ft.colors.WHITE), margin=1,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.INDIGO,
                    width=150,
                    height=25,
                    border_radius=5,
                    ),
                ft.Container(content=ft.Text(precio,color=ft.colors.WHITE), margin=1,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.INDIGO,
                    width=70,
                    height=25,
                    border_radius=5,
                    ),
                ft.Container(content=ft.Text(iva,color=ft.colors.WHITE), margin=1,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.INDIGO,
                    width=35,
                    height=25,
                    border_radius=5,
                    ),
                ft.Row(
                    spacing=0,
                    controls=[
                        
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Eliminar",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
                
            ],
        )
        
        return ft.Column(controls=[self.display_view])
        self.update()


    def delete_clicked(self, e):
        self.task_delete(self)

class TodoApp(ft.UserControl):
    def build(self):
        
        self.new_task = ft.TextField(hint_text="Escriba el id del producto", expand=True)
        
        self.tasks = ft.Column()
        
        # application's root control (i.e. "view") containing all other controls
        return ft.Column(
            width=350,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.tasks,
            ],
        )

    def add_clicked(self, e):
        print(f"{self.new_task.value} {max_productos}")
        if int(self.new_task.value) <= 0 or int(self.new_task.value) > max_productos:
            self.new_task.error_text = "No se encuentra en la base de datos"
            self.update()
        else:
            task = Task(self.new_task.value, self.task_delete)
            self.tasks.controls.append(task)
            self.new_task.error_text = ""
            self.update()
            

        

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()
def check_item_clicked(e):
    e.control.checked = not e.control.checked

#!==================MAIN==========================
def main(page: ft.Page):    
    page.window_full_screen=True
    page.theme = ft.Theme(color_scheme_seed="INDIGO",use_material3=True)
    #!Campos a llenar 
    
    Nombre_Cliente=ft.TextField(label="Nombre de Usuario",width=270,height=45,hint_text=("Ejm:Stiven Brandom"))
    Apeliido_Usuaio=ft.TextField(label="Apellido de Usuario",width=270,height=45,hint_text=("Ejm:Andrade Mazon"))
    Cedula=ft.TextField(label="Cedula",width=550,height=65,max_length=10,hint_text=("Ejm:1750395012"))
    Mail=ft.TextField(label="E-Mail",width=550,height=45,hint_text=("Ejm:Billify@gmail.com"))
    Direccion=ft.TextField(label="Direccio",width=550,height=45,hint_text=("Ejm:Cacha-Geovani Calles"))
    Telefono=ft.TextField(label="Telefono",width=550,height=45,hint_text=("Ejm:0979752578"))
    
    greetings = ft.Column()
    #!Campos del login
    
    Login_Usuario=ft.TextField(label="Usuario",width=550,height=70, autofocus=True)
    Registrar = ft.Column()
    Login_Pasword=ft.TextField(label="Contraseña",width=550,height=70,password=True,can_reveal_password=True,     )

    #!Campo para el Forget password
    Olvido_Contraseña=ft.TextField(label="Correo Electronico",width=500,height=80)

    #!Campos para Datos del Usuario
    Nombre_Usuario=ft.Text("  ",size=50)

    Primer_Nombre=ft.Text("  ",size=20)
    Segundo_Nombre=ft.Text("  ",size=20)
    Primer_Apellido=ft.Text("  ",size=20)
    Segundo_Apellido=ft.Text("  ",size=20)
    Cedula_Usuario=ft.Text("  ",size=20)
    Numero_Empleado=ft.Text("  ",size=20)
    Sede=ft.Text("  ",size=20)
    page.update()

    #!campos para editar
    Text_Primer_Nombre=ft.TextField(label="Primer Nombre",height=40,width=200)
    text_segundo_nombre=ft.TextField(label="Segundo Nombre",height=40,width=200)
    text_primer_apellido=ft.TextField(label="Primer Apellido",height=40,width=200)
    text_segundo_apellido=ft.TextField(label="Segundo Apellido",height=40,width=200)
    N_celula_empleado=ft.TextField(label="Ingresa tu numero de cedula",height=60,width=420,max_length=10)
    N__empleado=ft.TextField(label="Ingresa tu numero de Empleado",height=40,width=420)
    Lugar_sede=ft.TextField(label="Nombre de Sede",height=40,width=420)
    

    #!Tema y Titulo de la pagina
    page.theme_mode = ft.ThemeMode.LIGHT
    
    #!Funcion para cerrar el programa
    def Close(end):
        page.window_destroy()
        page.update()

    #! Funcion para Cambiar tema
    def theme(Luz):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode=ft.ThemeMode.LIGHT
        else:
            page.theme_mode=ft.ThemeMode.DARK
        page.update()
    #!Campo para cambiar la foto del Usuario
    Foto_Usuario=ft.Image(
        src=f"https://i.ibb.co/SfDkVwG/klipartz-com.png",
        width=500,
        height=200,
        border_radius=100,
    )
    Foto_Usuario_2=ft.Image(
        src=f"https://i.ibb.co/SfDkVwG/klipartz-com.png",
        width=360,
        height=200,
        border_radius=300,
    )
    def on_result(e: ft.FilePickerResultEvent):
        global img_path
        img_path = e.files[0].path
        Foto_Usuario.src = img_path
        Foto_Usuario_2.src=img_path
        Foto_Usuario.update()
        Foto_Usuario_2.update()
        # Borrar la lista de controles antes de añadir la nueva imagen
        page.update()

    pick_files_dialog = ft.FilePicker(on_result=on_result)

    page.overlay.append(pick_files_dialog)

    #!============------------------ALERTAS--------------------=================
    #!Alerta pra el boton de registrarse
    def close_registro(e):
        pop_registro.open = False
        page.update()

    def Close_revisa_correo_registro(e):
        mensaje_de_enviado_correo.open = False
        page.dialog = mensaje_de_enviado_correo
        mensaje_de_enviado_correo.open = True
        page.update()

    def close_dlg_mensaje_correo_enviado(e):
        mensaje_de_enviado_correo.open = False
        page.update()

    mensaje_de_enviado_correo= ft.AlertDialog(
        modal=True,
        title=ft.Text("Revisa tu correo!",size=30),
        content=ft.Text("tu usuario ha sido enviado",size=15),
        actions=[
            ft.FilledButton("Volver al menu", on_click=close_dlg_mensaje_correo_enviado),
        ],
        on_dismiss=lambda e: print("Dialog dismissed!"),
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )
    page.update()

    pop_registro=ft.AlertDialog(
        modal=True,
        title=ft.Text("Ingresa tu correo empresarial                         ",size=30),
        content=ft.Text("Recuerda,si no tienes un correo empresarial\nno podra realizar el registro.",size=20),
        actions=[
            ft.Column(
                [
                    ft.Divider(),
                    ft.TextField(
                        label="Ingresa tu correo",
                    ),
                    ft.Divider(),
                    ft.Row(
                        [
                            ft.FilledButton(
                                text="Cancelar",
                                on_click=close_registro,  
                            ),
                            ft.FilledButton(text="Enviar",
                                on_click=Close_revisa_correo_registro,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    )
                ]
            )
        ],
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    def open_dlg_pop_registro(e):
        page.dialog = pop_registro
        pop_registro.open = True
        page.update()
    #!Alerta de reportar problema
    def close_Reporte_problemas(e):
        Reporte_problemas.open = False
        page.update()

    def Close_and_open_gracias(e):
        Reporte_problemas.open = False
        page.dialog = Mensaje_de_gracias
        Mensaje_de_gracias.open = True
        page.update()

    def close_dlg_mensaje_gracias(e):
        Mensaje_de_gracias.open = False
        page.update()

    Mensaje_de_gracias = ft.AlertDialog(
        modal=True,
        title=ft.Text("Muchas gracias por tu colaboración!",size=30),
        content=ft.Text("haremos lo posible para solucionarlo",size=15),
        actions=[
            ft.FilledButton("Volver al menu", on_click=close_dlg_mensaje_gracias),
        ],
        on_dismiss=lambda e: print("Dialog dismissed!"),
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )
    page.update()

    Reporte_problemas=ft.AlertDialog(
        modal=True,
        title=ft.Text("Reporte de problemas"),
        content=ft.Text("Por favor selecciona el problema junto a una descripción"),
        actions=[
            ft.Column(
                [
                    ft.Divider(),
                    ft.Checkbox(label="Problema de rendimiento", value=False),
                    ft.Checkbox(label="Error en mostrar datos", value=False),
                    ft.Checkbox(label="Error en el manejo de ventanas", value=False),
                    ft.Checkbox(label="Problemas de bugs", value=False),
                    ft.Checkbox(label="Calculos incorrectos", value=False),
                    ft.Checkbox(label="Otros...", value=False),
                    ft.TextField(
                        label="Describe el problema",
                        multiline=True,
                        max_length=250,
                        max_lines=5,
                    ),
                    ft.Row(
                        [
                            ft.FilledButton(
                                text="Volver",
                                on_click=close_Reporte_problemas,  
                            ),
                            ft.FilledButton(text="Enviar",
                                on_click=Close_and_open_gracias,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                ]
            )
        ],
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    def open_dlg_modal_3(e):
        page.dialog = Reporte_problemas
        Reporte_problemas.open = True
        page.update()

    #!Alerta de cerrar secion
    def close_alert_cerrar_secion(e):
        Alert_cerrar_secion.open = False
        page.update()
    
    def close_alert_and_go_login(e):
        Alert_cerrar_secion.open = False
        page.go("/")
        page.update()

    Alert_cerrar_secion = ft.AlertDialog(
        modal=True,

        title=ft.Text("Por favor confirma"),
        content=ft.Text("Estas seguro de cerrar esta sesión?"),
        actions=[
            ft.TextButton("Si", on_click=close_alert_and_go_login),
            ft.TextButton("No", on_click=close_alert_cerrar_secion),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    
    def open_Alert_cerrar_secion(e):
        page.dialog = Alert_cerrar_secion
        Alert_cerrar_secion.open = True
        page.update()

    
    #!alerta de cerrar app
    def close_dlg_modal_2(e):
        dlg_modal_2.open = False
        page.update()

    dlg_modal_2 = ft.AlertDialog(
        modal=True,

        title=ft.Text("Por favor confirma"),
        content=ft.Text("Estas seguro de cerrar la aplicación?"),
        
        actions=[
            ft.TextButton("Sí", on_click=Close),
            ft.TextButton("No", on_click=close_dlg_modal_2),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    
    def open_dlg_modal_2(e):
        page.dialog = dlg_modal_2
        dlg_modal_2.open = True
        page.update()



    #!editar Usuario
    def Controles_editar_usuario(a):
        Primer_Nombre.value=Text_Primer_Nombre.value
        Segundo_Nombre.value=text_segundo_nombre.value
        Primer_Apellido.value=text_primer_apellido.value
        Segundo_Apellido.value=text_segundo_apellido.value
        Cedula_Usuario.value=N_celula_empleado.value
        Numero_Empleado.value=N__empleado.value
        Sede.value=Lugar_sede.value

        Editar_Usuario.open = False
        page.dialog = Mensaje_confirmar_datos
        Mensaje_confirmar_datos.open = True
        page.update()


    def open_Editar_Usuario(e):
        page.dialog =Editar_Usuario
        Editar_Usuario.open = True
        page.update()

    def close_dlg_editar_usuario(e):
        Editar_Usuario.open = False
        page.update()

    def close_dlg_mensaje_confirmar(e):
        Mensaje_confirmar_datos.open = False
        page.update()

    Editar_Usuario = ft.AlertDialog(
        modal=True,
        title=ft.Text("Editar datos"),
        content=ft.Text("Ingresa tus datos                               ",size=25),
        actions=[
            ft.Column(
                [
                    ft.Divider(),
                    ft.Text("Nombres:",size=20),
                    ft.Row(
                        [
                            Text_Primer_Nombre,text_segundo_nombre
                        ]
                    ),
                    ft.Text("Apellidos:",size=20),
                    ft.Row(
                        [
                            text_primer_apellido,text_segundo_apellido
                        ]
                    ),
                    ft.Divider(),
                    ft.Text("Ingrese sus identificadores:",size=20),
                    N_celula_empleado,N__empleado,Lugar_sede,
                    ft.Divider(),
                    ft.Row(
                        [
                            ft.FilledButton(
                                text="Cancelar",
                                on_click=close_dlg_editar_usuario,  
                            ),
                            ft.FilledButton(
                                text="Editar",
                                on_click=Controles_editar_usuario,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    
                ]
            ),
            
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )
    page.update()

    
    Mensaje_confirmar_datos = ft.AlertDialog(
        modal=True,
        title=ft.Text("Datos editados correctamente!"),
        actions=[
            ft.FilledButton("Volver al menu", on_click=close_dlg_mensaje_confirmar),
        ],
        on_dismiss=lambda e: print("Dialog dismissed!"),
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )
    page.update()

    #!REVISA TU CORREO
    def close_revisa_corre(e):
        Revisa_correo.open = False
        page.update()
    
    Revisa_correo=ft.AlertDialog(
        modal=True,
        title=ft.Text("Clave enviada exitosamente"),
        content=ft.Text("Por favor revisa tu correo",size=20),
        actions=[
            ft.FilledButton("Volver",
                on_click=close_revisa_corre,
            )
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )

    def open_revisa_correo(e):
        page.dialog =Revisa_correo
        Revisa_correo.open = True
        page.update()
    #!----------------------HOTKEYS------------------------------
    def on_keyboard(e: ft.KeyboardEvent):
        
        if (e.ctrl == True and e.key == "1"):
            print(
                f"Key: {e.key}, Control: {e.ctrl}"
            )
            
        if e.ctrl == True and e.key == "1":
            content.controls.pop()
            content.controls.append(page_one_ui)
            page.navigation_bar.selected_index = 0
            
            

        if e.ctrl == True and e.key == "2":
            content.controls.pop()
            content.controls.append(page_two_ui)
            page.navigation_bar.selected_index = 1
            

        if e.ctrl == True and e.key == "3":
            content.controls.pop()
            content.controls.append(page_three_ui)
            page.navigation_bar.selected_index = 2
        
        if e.ctrl == True and e.key == "4":
            content.controls.pop()
            content.controls.append(page_four_ui)
            page.navigation_bar.selected_index = 3
        


        page.update()
    page.on_keyboard_event = on_keyboard

    
    #!Genera un campo para registrarte
    def Sing(a):
        Registrar.controls.append(ft.Column([ft.TextField(label="Correo Electronico",width=380,height=45)]))
        page.update()
    #!funcion del enter del login para guardar el value y entrar al home
    def Usuario_fun(e):
        Nombre_Usuario.value=Login_Usuario.value
        page.go("/Home")
        page.update()
    #!Funcion para editar todo del login


    #!-------------CARTA DEL LOGIN---------------
    Login_Card=ft.Card(           
        width=600,
        height=500,
        elevation=15,
        content=ft.Container(

            border_radius=6,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Divider(height=20, color="transparent"),
                    ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=5,
                        controls=[
                            ft.Text("Inicia en Billify", size=40, weight="bold"),
                            ft.Text(
                                "Agrega tu usuario",
                                size=13,
                                weight="bold",
                            ),

                            ft.Divider(height=25, color="transparent"),
                            Login_Usuario,
                            #ft.Divider(height=0.5, color="transparent"),
                            Registrar,
                            #ft.Divider(height=0.5, color="transparent"),
                            Login_Pasword,
                            ft.Divider(height=0.1, color="transparent"),
                        ],
                    ),
                    ft.Row(
                        #width=320,
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.TextButton(
                                content=ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(value="Olvido la Cotraseña?", size=13),
                                        ],
                                    )
                                ),
                                on_click=lambda _: page.go("/Forgot_Password")    
                            )
                        ],
                    ),
                    ft.Divider(height=3, color="transparent"),
                    ft.FilledButton("Entrar", on_click=Usuario_fun,width=270,height=50),
                    #ft.Divider(height=35, color="transparent"),
                    ft.ElevatedButton("Registrarse", on_click=open_dlg_pop_registro,width=270,height=50,bgcolor=ft.colors.GREEN_500,color="WHITE"),
                ],
            ),
        ),
    )
    #!Card del forgot password
    Forgot_password=ft.Card(
        width=600,
        height=400,
        content=ft.Container(

            border_radius=6,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            ft.TextButton(
                                "Volver a Iniciar seción", icon="ARROW_BACK",
                                on_click=lambda _: page.go("/"),   
                                
                            ),
                            ft.Divider(height=10),
                        ]
                    ),
                    ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=5,
                        controls=[
                            ft.Text("Recupera tu cuenta",size=45),
                            ft.Divider(height=20,color="transparent"),
                            ft.Text("Introduce tu correo electrónico",size=20),
                            ft.Divider(height=25,color="transparent"),
                            Olvido_Contraseña,ft.Divider(height=9,color="transparent"),
                            ft.FilledButton("Buscar Cuenta",width=150,height=50,on_click=open_revisa_correo),
                            
                        ],
                    ),
                ],
            ),
        ),
    )
    
    #!Card del Usuario
    Usuario=ft.Card(
        width=1350,
        height=700,
        content=ft.Container(

            border_radius=6,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            #ft.Divider(height=10),
                        ]
                    ),
                    ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=5,
                        controls=[
                            Foto_Usuario,
                            ft.Row(
                                [
                                    ft.ElevatedButton(
                                        "Cambiar imagen",
                                        icon=ft.icons.ADD_PHOTO_ALTERNATE_OUTLINED,
                                        on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True),
                                    ),
                                    ft.ElevatedButton(
                                        "Editar credenciales",
                                        icon=ft.icons.EDIT,
                                        on_click=open_Editar_Usuario,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),

                            #!usuario y files
                            Nombre_Usuario,
                            #!Card de los Datos
                            ft.Container(
                                width=500,
                                height=280,
                                border_radius=20,
                                shadow=ft.BoxShadow(
                                    spread_radius=1,
                                    blur_radius=15,
                                    offset=ft.Offset(0, 0),
                                    blur_style=ft.ShadowBlurStyle.OUTER,
                                ),
                                content=ft.Container(
                                    border_radius=6,
                                    content=ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Row(
                                                [
                                                    ft.VerticalDivider(width=50),
                                                    ft.Column(
                                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.Row(
                                                                [
                                                                    ft.Column(
                                                                        [
                                                                            ft.Text("Nombre:",size=20,),
                                                                            ft.Text("Segundo Nombre:",size=20),
                                                                            ft.Text("Primer Apellido:",size=20),
                                                                            ft.Text("Segundo Apellido:",size=20),
                                                                            ft.Text("Cedula:",size=20),
                                                                            ft.Text("N. de empleado",size=20),
                                                                            ft.Text("Sede:",size=20),
                                                                        ]
                                                                    ),
                                                                    ft.VerticalDivider(width=50),
                                                                    ft.Column(
                                                                        [
                                                                            Primer_Nombre,Segundo_Nombre,Primer_Apellido,Segundo_Apellido,
                                                                            Cedula_Usuario,Numero_Empleado,Sede,
                                                                        ]
                                                                    ),
                                                                ]
                                                            )
                                                        ],
                                                    ),
                                                ]
                                            )
                                        ],
                                    ),
                                ),
                            )
                        ],
                    ),
                ],
            ),
        ),
    )
    #!Carta de los datos del Usuario

    #!Rail de la izquierda
    Nav_Izquierdo=ft.Container(
        width=180,
        height=600,
        border_radius=10,
        content=ft.Card(
            width=180,
            height=600, 
            
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=(
                    [
                        ft.Divider(height=10,color=ft.colors.TRANSPARENT),
                        Foto_Usuario_2,
                        ft.Divider(color="BLUE"),
                        ft.Column(
                            [
                                ft.Row([ft.Text(""),Primer_Nombre,Primer_Apellido]),
                                ft.Row([ft.Text(""),Cedula_Usuario]),
                                ft.Row([ft.Text(""),Sede])
                            ],
                            
                        ),
                        ft.Divider(height=10),
                        ft.Text("Codigo QR de Usuario",size=15,weight=ft.FontWeight.W_900),
                        ft.Divider(height=1,color=ft.colors.TRANSPARENT),
                        ft.Container(
                                width=150,
                                height=150,
                                border_radius=20,
                                shadow=ft.BoxShadow(
                                    spread_radius=1,
                                    blur_radius=1,
                                    offset=ft.Offset(0, 0),
                                    blur_style=ft.ShadowBlurStyle.OUTER,
                                ),
                                content=ft.Container(
                                    ft.Column(
                                        [
                                            ft.Image(
                                                src=f"Qr_usuario.png",
                                                width=180,
                                            )
                                        ],
                                        alignment=ft.CrossAxisAlignment.CENTER
                                    ),
                                
                                )
                            )
                    ]
                ),
                
            ),
        ),
    ) 
    page.update()


    Datos_container_datos=ft.Row(
        [   
            ft.Column(
                [
                    ft.Text("Datos de Usuario",size=40),
                    ft.Row(controls=[Nombre_Cliente,Apeliido_Usuaio]),
                    Mail,Direccion,Cedula,Telefono,ft.FilledButton("Enviar datos")
                ],
                scroll=ft.ScrollMode.ADAPTIVE
            ),  
        ]
    )
    #!----------------CARDS DEL HOME--------------------------
    Container_datos=ft.Container(
        width=1150,
        height=620,
        content=ft.Row(
            [
                ft.Card(
                    width=575,
                    height=610,
                    content=ft.Row(
                        [
                            
                            ft.VerticalDivider(width=2,color=ft.colors.TRANSPARENT),
                            ft.Column(
                                [
                                    Datos_container_datos
                                ]
                            ),
                        ],
                        scroll=ft.ScrollMode.ADAPTIVE
                    ),   
                ),
        
                ft.Card(
                    width=575,
                    height=610,
                    content=ft.Row(
                        [
                            
                            ft.VerticalDivider(width=2,color=ft.colors.TRANSPARENT),
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text("Ingrese el ID del producto",size=35),
                                            TodoApp(),
                                        ],
                                        scroll=ft.ScrollMode.ADAPTIVE, alignment=ft.MainAxisAlignment.START , height=600, width=500
                                    ),  
                                ],  
                            )  
                        ],
                    ),   
                ),
                
            ],
        )
    )
    #!DATATABLES
    Data_table=ft.DataTable(
        width=1100,

        columns=[
            ft.DataColumn(ft.Text("ID"),),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Precio Unidad")),
            ft.DataColumn(ft.Text("IVA")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("1")),
                    ft.DataCell(ft.Text("Arroz")),
                    ft.DataCell(ft.Text("2.5")),
                    ft.DataCell(ft.Text("No")),
                    
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("2")),
                    ft.DataCell(ft.Text("Aceite de cocina")),
                    ft.DataCell(ft.Text("3.2")),
                    ft.DataCell(ft.Text("12%")),
                    
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("3")),
                    ft.DataCell(ft.Text("Café")),
                    ft.DataCell(ft.Text("4.5")),
                    ft.DataCell(ft.Text("No")),
                    
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("4")),
                    ft.DataCell(ft.Text("Leche")),
                    ft.DataCell(ft.Text("1.8")),
                    ft.DataCell(ft.Text("No")),
                    
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("5")),
                    ft.DataCell(ft.Text("Chocolate")),
                    ft.DataCell(ft.Text("1.25")),
                    ft.DataCell(ft.Text("12%")),
                    
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("6")),
                    ft.DataCell(ft.Text("Huevos")),
                    ft.DataCell(ft.Text("0.3")),
                    ft.DataCell(ft.Text("No")),
                    
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("7")),
                    ft.DataCell(ft.Text("Pan")),
                    ft.DataCell(ft.Text("0.7")),
                    ft.DataCell(ft.Text("No")),
                    
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("8")),
                    ft.DataCell(ft.Text("Pasta")),
                    ft.DataCell(ft.Text("1.6")),
                    ft.DataCell(ft.Text("No"    )),
                    
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("9")),
                    ft.DataCell(ft.Text("galletas")),
                    ft.DataCell(ft.Text("1.2")),
                    ft.DataCell(ft.Text("12%"    )),
                    
                ],
            ),
        ],
        
    )

    Data_table_historial=ft.DataTable(
        width=1200,

        columns=[
            ft.DataColumn(ft.Text("ID"),),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Cedula")),
            ft.DataColumn(ft.Text("IVA")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("1")),
                    ft.DataCell(ft.Text("Arroz")),
                    ft.DataCell(ft.Text("xxxxx")),
                    ft.DataCell(ft.Text("No")),
                    
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("2")),
                    ft.DataCell(ft.Text("Aceite de cocina")),
                    ft.DataCell(ft.Text("3.2")),
                    ft.DataCell(ft.Text("12%")),
                    
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("3")),
                    ft.DataCell(ft.Text("Café")),
                    ft.DataCell(ft.Text("4.5")),
                    ft.DataCell(ft.Text("No")),
                    
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("4")),
                    ft.DataCell(ft.Text("Leche")),
                    ft.DataCell(ft.Text("1.8")),
                    ft.DataCell(ft.Text("No")),
                    
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("5")),
                    ft.DataCell(ft.Text("Chocolate")),
                    ft.DataCell(ft.Text("1.25")),
                    ft.DataCell(ft.Text("12%")),
                    
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("6")),
                    ft.DataCell(ft.Text("Huevos")),
                    ft.DataCell(ft.Text("0.3")),
                    ft.DataCell(ft.Text("No")),
                    
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("7")),
                    ft.DataCell(ft.Text("Pan")),
                    ft.DataCell(ft.Text("0.7")),
                    ft.DataCell(ft.Text("No")),
                    
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("8")),
                    ft.DataCell(ft.Text("Pasta")),
                    ft.DataCell(ft.Text("1.6")),
                    ft.DataCell(ft.Text("No"    )),
                    
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("9")),
                    ft.DataCell(ft.Text("galletas")),
                    ft.DataCell(ft.Text("1.2")),
                    ft.DataCell(ft.Text("12%"    )),
                    
                ],
            ),
        ],
        
    )

    #!PAGINAS
    
    page_one_ui = ft.Row(
        [     
            ft.Row(
                [
                    Nav_Izquierdo,
                    Container_datos,
                ],
                alignment=ft.CrossAxisAlignment.START, 
            ),  
        ],  
    )

    page_two_ui = ft.Row(
        [
            ft.Row(
                [
                    ft.VerticalDivider(width=70),
                    ft.Column(
                        [
                            ft.Text("Inventario",size=40),
                            ft.TextField(label="Buscar Producto por ID o nombre",
                                width=400,prefix_icon=ft.icons.SEARCH,
                            ),
                            Data_table
                        ]
                        
                    )
                ],
                alignment=ft.CrossAxisAlignment.CENTER   
            ),          
        ],       
    )  

    page_three_ui = ft.Row(
        [
            ft.Row(
                [   
                    ft.VerticalDivider(width=70),
                    ft.Column(
                        [
                            ft.Text("Historial de Facturas",size=40),
                            ft.Row(
                                [
                                    ft.TextField(label="Buscar por N.Factura",prefix_icon=ft.icons.RECEIPT_LONG_SHARP),
                                    ft.VerticalDivider(),ft.TextField(label="Buscar por nombre de cliente",prefix_icon=ft.icons.PERSON_PIN_OUTLINED),
                                    ft.VerticalDivider(),ft.TextField(label="Fecha de emisión de la factura",prefix_icon=ft.icons.DATE_RANGE)
                                ]
                            ),
                            Data_table_historial,
                        ]
                    )
                    
                ],
                alignment=ft.CrossAxisAlignment.CENTER   
            )
        ]
    )
    page_four_ui = ft.Row(
        [
            ft.Row(
                [
                    Usuario,
                ]
            )
        ]
    )

    content = ft.Row([page_one_ui])

    #!Cambia ventana con el Nav_Bar de abajo
    def change_index(e):
        index = page.navigation_bar.selected_index
        print(str(index))

        if index == 0:
            content.controls.pop()
            content.controls.append(page_one_ui)
            

        if index == 1:
            content.controls.pop()
            content.controls.append(page_two_ui)
        if index == 2:
            content.controls.pop()
            content.controls.append(page_three_ui)
        if index == 3:
            content.controls.pop()
            content.controls.append(page_four_ui)
        
        page.update()
        
    #!------------------------Nab_bar----------------------------
    page.navigation_bar = ft.NavigationBar(
        on_change=change_index,
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.HOME_OUTLINED,
                selected_icon=ft.icons.HOME_ROUNDED,
                label="Menu principal",
            ),
            ft.NavigationDestination(
                icon=ft.icons.INVENTORY_2_OUTLINED,
                selected_icon=ft.icons.INVENTORY_2_ROUNDED,
                label="Inventario",
            ),
            ft.NavigationDestination(
                icon=ft.icons.ACCOUNT_BALANCE_OUTLINED,
                selected_icon=ft.icons.ACCOUNT_BALANCE_ROUNDED,
                label="Balance",
            ),
            ft.NavigationDestination(
                icon=ft.icons.ACCOUNT_CIRCLE_OUTLINED,
                selected_icon=ft.icons.ACCOUNT_CIRCLE,
                label="Usuario",
            ),
        ],
        height=70,
    )
    #!APPBAR
    page.appbar = ft.AppBar(         
        leading_width=40,
        title=ft.Text("BILLIFY",weight=bool,size=30),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(
                ft.icons.WB_SUNNY_OUTLINED,
                selected_icon=ft.icons.BOOKMARK,
                tooltip=("Modo Oscuro"),
                on_click=theme,
            ),
            ft.PopupMenuButton(
                tooltip="Menu",
                items=[
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text=("Reportar Error"),
                        icon=ft.icons.ERROR,
                        #on_click=lambda _: page.go("/"),
                        on_click=open_dlg_modal_3,
                    ),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text=("Cerrar sesión"),
                        icon=ft.icons.MANAGE_ACCOUNTS,
                        #on_click=lambda _: page.go("/"),
                        on_click=open_Alert_cerrar_secion,
                    ),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        icon=ft.icons.EXIT_TO_APP,
                        text=("Salir"),
                        on_click=open_dlg_modal_2,
                    ),
                ]
            ),
        ],
    )
    #!----------------------------------CAMBIO DE VENTANAS----------------------
    def route_change(e):
        page.horizontal_alignment = "center",
        page.vertical_alignment = "center" , 
        page.views.clear()
        if page.route == "/":
            page.views.append(
            #!Login
            ft.View(
                "/",
                [   
                    ft.Divider(height=50, color="transparent"),
                    ft.Row(
                        [
                            ft.VerticalDivider(width=50,color="transparent"),
                            ft.Column(
                                [
                                    ft.Column(
                                        [
                                            ft.Container(
                                                width=550,
                                                height=250,
                                                content=ft.Row(
                                                    [
                                                        #ft.VerticalDivider(width=200),    
                                                        ft.Column(
                                                            [
                                                                ft.Image(
                                                                    src=f"New_Logo.png",
                                                                    width=288,
                                                                ),
                                                                #ft.Text("Inicia secion en Billify")
                                                            ],
                                                            #alignment=ft.MainAxisAlignment.START
                                                        ), 
                                                    ],
                                                    
                                                ),
                                            ),
                                            ft.Container(
                                                width=600,
                                                height=350,
                                                content=ft.Column(
                                                    [
                                                        ft.Text("Billify", size=75, weight=ft.FontWeight.W_900, selectable=True,color=ft.colors.BLUE_600),
                                                        ft.Text("Factura fácil, negocio ágil", size=40, weight=ft.FontWeight.W_900, selectable=True,color=ft.colors.GREY_800),
                                                        ft.Text("", size=50, weight=ft.FontWeight.W_900, selectable=True,color=ft.colors.BLUE_600),
                                                    ]
                                                )
                                            )
                                        ],
                                    ),
                                ]
                            ),
                            #ft.VerticalDivider(width=300,color="transparent"),
                            ft.Container(
                                ft.Row(
                                    [
                                        Login_Card,
                                        #ft.VerticalDivider(width=60,color="transparent"),
                                    ],
                                    alignment=ft.MainAxisAlignment.END,
                                )
                            )
                        ]
                    )      
                ]
            )
        )
        #!Home
        elif page.route == "/Home":
            
            page.views.append(
                ft.View(
                    "/Home",
                    [     
                        page.appbar,
                        
                        page.navigation_bar,
                        ft.Column(
                            [
                                content,greetings,
                            ],
                            alignment=(ft.MainAxisAlignment.START)
                        )    
                    ]     
                )
                
            )
        elif page.route=="/Forgot_Password":
            page.views.append(
            #!Login_forgot
                ft.View(
                    "/Forgot_Password",
                    [   
                        ft.Row(
                            [   
                                ft.Column(
                                    [
                                        ft.Divider(height=120),
                                        Forgot_password,
                                    ],
                                    alignment=(ft.MainAxisAlignment.CENTER)
                                )
                            ],
                            alignment=(ft.MainAxisAlignment.CENTER)
                        )
                    ]
                )
            )
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)