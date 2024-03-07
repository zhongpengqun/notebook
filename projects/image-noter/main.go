package main

import (
	"fmt"
	"image/color"
	"log"

	g "github.com/AllenDang/giu"
	"github.com/sqweek/dialog"
)

var (
	row *g.ColumnWidget = g.Column()
	img *g.ImageWithRgbaWidget
	col = color.RGBA{}
)

func onClickMe() {
	filename, _ := dialog.File().Filter("Image", "png").Load()
	log.Printf("Chosen file: %s\n", filename)

	rgba, _ := g.LoadImage(filename)

	img = g.ImageWithRgba(rgba).OnClick(func() {
		fmt.Println("rgba image was clicked")

		clickedPos := g.GetMousePos().Sub(g.GetCursorPos())
		col = rgba.RGBAAt(clickedPos.X, clickedPos.Y)

		fmt.Println("x:", clickedPos.X)
		fmt.Println("y:", clickedPos.Y)

		fmt.Printf("rgba(%v,%v,%v,%v)", col.R, col.G, col.B, col.A)

		row = g.Column(
			img,
			g.ColorEdit("chosen color", &col),
		)
	}).Size(float32(rgba.Rect.Max.X), float32(rgba.Rect.Max.Y))

	row = g.Column(
		img,
	)
}

func loop() {
	g.SingleWindow().Layout(
		g.Row(
			g.Button("Pick image").OnClick(onClickMe),
		),
		row,
	)
}

func main() {
	fmt.Println("-----")
	wnd := g.NewMasterWindow("Image color picker", 1080, 720, g.MasterWindowFlagsNotResizable)
	fmt.Println("=====")
	wnd.Run(loop)
}
