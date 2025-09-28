import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
from datetime import datetime

ARCHIVO_AGENDA = "agenda_medicinas.json"

class Medicina:
    def __init__(self, nombre, dosis, horario, dias, tomado=False, fecha_inicio=None):
        self.nombre = nombre
        self.dosis = dosis
        self.horario = horario
        self.dias = dias
        self.tomado = tomado
        self.fecha_inicio = fecha_inicio or datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "dosis": self.dosis,
            "horario": self.horario,
            "dias": self.dias,
            "tomado": self.tomado,
            "fecha_inicio": self.fecha_inicio,
        }

    @staticmethod
    def from_dict(data):
        return Medicina(
            data["nombre"],
            data["dosis"],
            data["horario"],
            data["dias"],
            data.get("tomado", False),
            data.get("fecha_inicio", datetime.now().strftime("%Y-%m-%d"))
        )

class AgendaMedicinasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Medicinas")
        self.medicinas = []

        self.cargar_agenda()
        self.crear_interfaz()
        self.actualizar_lista()

    def crear_interfaz(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        # Campos de entrada
        tk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky="e")
        self.entry_nombre = tk.Entry(frame)
        self.entry_nombre.grid(row=0, column=1)

        tk.Label(frame, text="Dosis:").grid(row=1, column=0, sticky="e")
        self.entry_dosis = tk.Entry(frame)
        self.entry_dosis.grid(row=1, column=1)

        tk.Label(frame, text="Horario (HH:MM):").grid(row=2, column=0, sticky="e")
        self.entry_horario = tk.Entry(frame)
        self.entry_horario.grid(row=2, column=1)

        tk.Label(frame, text="Duración (días):").grid(row=3, column=0, sticky="e")
        self.entry_dias = tk.Entry(frame)
        self.entry_dias.grid(row=3, column=1)

        # Botón Agregar
        tk.Button(frame, text="Agregar Medicina", command=self.agregar_medicina).grid(row=4, column=0, columnspan=2, pady=5)

        # Tabla de medicinas
        columnas = ("Nombre", "Dosis", "Horario", "Días", "Tomado")
        self.tree = ttk.Treeview(self.root, columns=columnas, show="headings", height=8)
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(pady=10)

        # Botón Marcar como tomado
        tk.Button(self.root, text="Marcar como Tomado", command=self.marcar_como_tomado).pack(pady=5)

    def agregar_medicina(self):
        nombre = self.entry_nombre.get().strip()
        dosis = self.entry_dosis.get().strip()
        horario = self.entry_horario.get().strip()
        dias = self.entry_dias.get().strip()

        # Validaciones
        if not nombre or not dosis or not horario or not dias:
            messagebox.showwarning("Campos incompletos", "Por favor completa todos los campos.")
            return

        try:
            datetime.strptime(horario, "%H:%M")
        except ValueError:
            messagebox.showerror("Formato de hora incorrecto", "El horario debe tener el formato HH:MM (ej. 08:30).")
            return

        try:
            dias = int(dias)
            if dias <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Días inválidos", "La duración debe ser un número entero mayor que 0.")
            return

        nueva_medicina = Medicina(nombre, dosis, horario, dias)
        self.medicinas.append(nueva_medicina)
        self.guardar_agenda()
        self.actualizar_lista()
        self.limpiar_campos()

    def actualizar_lista(self):
        self.tree.delete(*self.tree.get_children())

        for med in self.medicinas:
            self.tree.insert("", "end", values=(
                med.nombre,
                med.dosis,
                med.horario,
                med.dias,
                "Sí" if med.tomado else "No"
            ))

    def marcar_como_tomado(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Selecciona una medicina", "Selecciona una medicina para marcar como tomada.")
            return

        item = self.tree.item(seleccion[0])
        nombre = item["values"][0]

        for med in self.medicinas:
            if med.nombre == nombre:
                med.tomado = True
                break

        self.guardar_agenda()
        self.actualizar_lista()

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_dosis.delete(0, tk.END)
        self.entry_horario.delete(0, tk.END)
        self.entry_dias.delete(0, tk.END)

    def guardar_agenda(self):
        try:
            with open(ARCHIVO_AGENDA, "w", encoding="utf-8") as f:
                json.dump([m.to_dict() for m in self.medicinas], f, indent=4, ensure_ascii=False)
        except Exception as e:
            messagebox.showerror("Error al guardar", f"No se pudo guardar la agenda: {e}")

    def cargar_agenda(self):
        if os.path.exists(ARCHIVO_AGENDA):
            try:
                with open(ARCHIVO_AGENDA, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.medicinas = [Medicina.from_dict(d) for d in data]
            except Exception as e:
                messagebox.showerror("Error al cargar", f"No se pudo cargar la agenda: {e}")
                self.medicinas = []

# --- EJECUCIÓN ---
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaMedicinasApp(root)
    root.mainloop()
