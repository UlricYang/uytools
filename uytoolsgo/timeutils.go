package uytoolsgo

import (
	"strings"
	"time"
)

func now14() string {
	timeStr := time.Now().Format("2006-01-02 15:03:04")
	tags := []string{" ", "-", ":"}
	for _, item := range tags {
		timeStr = strings.Replace(timeStr, item, "", -1)
	}
	return timeStr
}
